"use client";

import { useState } from "react";
import { askQuestion } from "../lib/api";

export default function ChatWindow() {
  const [messages, setMessages] = useState<any[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const send = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", content: input };
    setMessages(prev => [...prev, userMsg]);

    setLoading(true);

    try {
      const answer = await askQuestion(input);

      const botMsg = { role: "bot", content: answer };
      setMessages(prev => [...prev, botMsg]);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { role: "bot", content: "⚠️ The ravens failed to return..." }
      ]);
    }

    setInput("");
    setLoading(false);
  };

  return (
    <div className="p-4 max-w-2xl mx-auto">
      
      {/* Chat Box */}
      <div className="h-[400px] overflow-y-auto border border-gray-700 p-4 rounded bg-black">
        {messages.map((m, i) => (
          <div key={i} className="mb-2">
            <b>{m.role === "user" ? "You" : "Maester"}:</b> {m.content}
          </div>
        ))}
        {loading && <div>🔥 Consulting the realm...</div>}
      </div>

      {/* Input */}
      <div className="flex mt-3 gap-2">
        <input
          className="flex-1 p-2 bg-gray-800 text-white border border-gray-600 rounded outline-none"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask the realm..."
          onKeyDown={(e) => {
            if (e.key === "Enter") send();
          }}
        />

        <button
          onClick={send}
          className="bg-red-700 px-4 rounded hover:bg-red-800"
        >
          Send
        </button>
      </div>
    </div>
  );
}
