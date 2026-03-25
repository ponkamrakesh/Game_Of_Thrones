import axios from "axios";

const API_URL = "https://game-of-thrones-ngda3gxpw-ponkamrakesh-gmailcoms-projects.vercel.app"; // change after deploy

export const askQuestion = async (question: string) => {
  const res = await axios.post(`${API_URL}/query`, { question });
  return res.data.answer;
};
