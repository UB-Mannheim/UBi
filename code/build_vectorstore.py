#!/usr/bin/env python

"""
Build or rebuild the vector database for local RAG.
Run this script whenever you update the markdown documents.

Usage:
    python build_vectorstore.py          # Build with default settings
    python build_vectorstore.py --force  # Force rebuild even if DB exists
"""

import argparse
import asyncio
import os
import re
import shutil
import sys
from pathlib import Path

from dotenv import load_dotenv

from config import CHUNK_OVERLAP, CHUNK_SIZE, PERSIST_DIR
from rag_local import create_rag_chain


async def build_vectorstore(force_rebuild: bool = False, incremental: bool = True):
    """Build the vector database."""

    # Check if using OpenAI vectorstore
    use_openai = os.getenv("USE_OPENAI_VECTORSTORE", "False").lower() == "true"
    if use_openai:
        print("❌ This script is only for local RAG (Ollama/Chroma).")
        print("   You're using OpenAI vectorstore according to .env")
        return False

    # Get embedding model info
    ollama_embedding_model = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")

    # Calculate persist path (same logic as rag_local.py)
    model_name = f"ollama_{re.sub(r'[^a-zA-Z0-9_-]', '_', ollama_embedding_model)}"
    persist_path = PERSIST_DIR / f"{model_name}_c{CHUNK_SIZE}_o{CHUNK_OVERLAP}_ub"

    # Check if DB already exists
    if persist_path.exists() and not force_rebuild:
        if incremental:
            print("📊 Vector database exists, checking for updates...")
            print(f"   Location: {persist_path}")
            print()
        else:
            print("✅ Vector database already exists at:")
            print(f"   {persist_path}")
            print("\n💡 Use --force to rebuild or --incremental to update")
            return True

    if force_rebuild and persist_path.exists():
        print(f"🗑️  Removing existing database at {persist_path}")
        shutil.rmtree(persist_path)

    # Build the database
    print("🔨 Building vector database...")
    print(f"   Embedding model: {ollama_embedding_model}")
    print(f"   Chunk size: {CHUNK_SIZE}")
    print(f"   Chunk overlap: {CHUNK_OVERLAP}")
    print()

    try:
        await create_rag_chain(debug=True)
        print()
        print("✅ Vector database built successfully!")
        print(f"   Location: {persist_path}")
        print("\n💡 The app will now load instantly on startup")
        return True
    except Exception as e:
        print("\n❌ Failed to build vector database:")
        print(f"   {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Build vector database for UBi chatbot"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force full rebuild even if database exists"
    )
    parser.add_argument(
        "--incremental",
        action="store_true",
        default=True,
        help="Use incremental updates (default: True)"
    )
    parser.add_argument(
        "--no-incremental",
        action="store_false",
        dest="incremental",
        help="Disable incremental updates, do full rebuild"
    )
    args = parser.parse_args()

    # Set environment variable for incremental mode
    os.environ["VECTORSTORE_INCREMENTAL"] = "true" if args.incremental else "false"

    # Load environment variables
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)

    success = asyncio.run(build_vectorstore(force_rebuild=args.force, incremental=args.incremental))
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
