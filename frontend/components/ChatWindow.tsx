"use client";

import { useState } from "react";
import { askQuestion } from "../lib/api";

export default function ChatWindow() {
  const [messages, setMessages] = useState<any[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const send = async () => {
    if (!input) return;

    setMessages(prev => [...prev, { role: "user", content: input }]);
    setLoading(true);

    const answer = await askQuestion(input);

    setMessages(prev => [...prev, { role: "bot", content: answer }]);
    setInput("");
    setLoading(false);
  };

  return (
    <div className="p-4">
      <div className="h-[400px] overflow-y-auto border p-2">
        {messages.map((m, i) => (
          <div key={i}>
            <b>{m.role}:</b> {m.content}
          </div>
        ))}
        {loading && <div>🔥 Consulting the realm...</div>}
      </div>

      <div className="flex mt-2">
        <input
          className="flex-1 p-2 bg-gray-800"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button onClick={send} className="bg-red-700 px-4">
          Send
        </button>
      </div>
    </div>
  );
}