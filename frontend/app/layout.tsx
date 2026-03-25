import "../styles/globals.css";

export const metadata = {
  title: "The Citadel Oracle",
  description: "Ask the realm",
};

export default function RootLayout({ children }: any) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}