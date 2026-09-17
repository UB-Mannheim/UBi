export default function AiNotice() {
  const language = String(props.language ?? "").trim().toLowerCase();
  const isGerman = ["german"].includes(language);

  return (
    <div className="mt-3 text-sm italic text-blue-700 dark:text-blue-400">
      {isGerman ? "KI-generierter Inhalt" : "AI-generated content"}
    </div>
  );
}