import OpenAI from "openai";

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ reply: "Method not allowed" });
  }

  try {
    const client = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });

    const { message } = req.body || {};

    if (!message || !message.trim()) {
      return res.status(400).json({ reply: "اكتب سؤالك هنا." });
    }

    const response = await client.responses.create({
      model: "gpt-4.1-mini",
      input: message,
    });

    return res.status(200).json({
      reply: response.output_text || "تعذر الرد على هذا السؤال.",
    });
  } catch (error) {
    return res.status(500).json({
      reply: "هناك خطأ في الاتصال بالذكاء الاصطناعي.",
    });
  }
}