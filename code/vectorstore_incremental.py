"""File index manager for incremental vector store updates."""

import hashlib
import json
from pathlib import Path
from typing import Dict, List, Tuple


class FileIndexManager:
    """Manages file index for incremental vector store updates."""

    def __init__(self, persist_path: Path):
        self.persist_path = persist_path
        self.index_file = persist_path / "file_index.json"
        self.index = self._load_index()

    def _load_index(self) -> dict:
        """Load file index from disk."""
        if self.index_file.exists():
            with open(self.index_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"files": {}, "config": {}}

    def save_index(self):
        """Save file index to disk."""
        self.persist_path.mkdir(parents=True, exist_ok=True)
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(self.index, f, indent=2)

    @staticmethod
    def compute_checksum(file_path: Path) -> str:
        """Compute MD5 checksum of file content."""
        md5 = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                md5.update(chunk)
        return md5.hexdigest()

    def detect_changes(
        self, current_files: List[Path]
    ) -> Tuple[List[Path], List[Path], List[str]]:
        """
        Detect file changes.

        Returns:
            (new_or_modified, unchanged, deleted_paths)
        """
        current_file_map: Dict[str, Path] = {
            str(f.resolve()): f for f in current_files
        }
        indexed_files = set(self.index["files"].keys())
        current_file_paths = set(current_file_map.keys())

        # Deleted files
        deleted = list(indexed_files - current_file_paths)

        # New or modified files
        new_or_modified = []
        unchanged = []

        for path_str, file_path in current_file_map.items():
            if path_str not in indexed_files:
                # New file
                new_or_modified.append(file_path)
            else:
                # Check if modified
                current_checksum = self.compute_checksum(file_path)
                indexed_checksum = self.index["files"][path_str].get(
                    "checksum", ""
                )

                if current_checksum != indexed_checksum:
                    new_or_modified.append(file_path)
                else:
                    unchanged.append(file_path)

        return new_or_modified, unchanged, deleted

    def update_file_entry(self, file_path: Path, chunk_ids: List[str]):
        """Update index entry for a file."""
        path_str = str(file_path.resolve())
        self.index["files"][path_str] = {
            "checksum": self.compute_checksum(file_path),
            "mtime": file_path.stat().st_mtime,
            "chunks": chunk_ids,
        }

    def remove_file_entry(self, file_path_str: str) -> List[str]:
        """Remove file from index and return its chunk IDs."""
        if file_path_str in self.index["files"]:
            chunk_ids = self.index["files"][file_path_str].get("chunks", [])
            del self.index["files"][file_path_str]
            return chunk_ids
        return []

    def get_chunk_ids_for_file(self, file_path_str: str) -> List[str]:
        """Get chunk IDs for a file."""
        return self.index["files"].get(file_path_str, {}).get("chunks", [])

    def update_config(
        self, chunk_size: int, chunk_overlap: int, embedding_model: str
    ):
        """Update configuration in index."""
        self.index["config"] = {
            "chunk_size": chunk_size,
            "chunk_overlap": chunk_overlap,
            "embedding_model": embedding_model,
        }

    def config_changed(
        self, chunk_size: int, chunk_overlap: int, embedding_model: str
    ) -> bool:
        """Check if configuration has changed."""
        current_config = self.index.get("config", {})
        return (
            current_config.get("chunk_size") != chunk_size
            or current_config.get("chunk_overlap") != chunk_overlap
            or current_config.get("embedding_model") != embedding_model
        )
