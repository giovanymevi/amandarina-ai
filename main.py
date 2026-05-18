from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import os
from scraper import get_site_context

app = FastAPI(title="Amandarina AI Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

class Message(BaseModel):
    text: str

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SITE_CONTEXT = get_site_context()

@app.get("/")
def health():
    return {"status": "ok", "message": "Amandarina AI is running"}

@app.post("/chat")
async def chat(msg: Message):
    system_prompt = f"""Eres el asistente virtual de AMANDARINA, agencia de soluciones digitales en Bucaramanga, Colombia.

Info de la empresa:
{SITE_CONTEXT}

Instrucciones:
- Responde en español, tono profesional y directo
- Servicios: Apps móviles iOS/Android, IA & Machine Learning, Blockchain, Software a medida
- Menciones clave: 100+ proyectos exitosos, 5+ años de experiencia, soporte 24/7
- Si preguntan precios: invita a contactar por WhatsApp o formulario
- Máximo 3 líneas. Si no sabes, di "te conecto con un asesor"
"""

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
                json={
                    "model": "llama-3.1-70b-versatile",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": msg.text}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 400
                }
            )
        data = r.json()
        return {"reply": data["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"reply": "Hubo un error. Te conecto con un asesor de AMANDARINA."}