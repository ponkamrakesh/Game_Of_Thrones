import axios from "axios";

const API_URL = "http://localhost:8000"; // change after deploy

export const askQuestion = async (question: string) => {
  const res = await axios.post(`${API_URL}/query`, { question });
  return res.data.answer;
};