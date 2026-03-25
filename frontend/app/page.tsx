import ChatWindow from "../components/ChatWindow";

export default function Home() {
  return (
    <main className="min-h-screen bg-black text-white">
      <h1 className="text-3xl text-center p-4">
        🐉 The Citadel Oracle
      </h1>
      <ChatWindow />
    </main>
  );
}