export default function MessageBubble({ role, content }: any) {
  return (
    <div className={`p-2 ${role === "user" ? "text-right" : "text-left"}`}>
      <span>{content}</span>
    </div>
  );
}