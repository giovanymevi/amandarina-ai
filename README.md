# Amandarina AI Agent

Chatbot inteligente para amandarina.com usando Groq API (Llama 3.1)

## Despliegue en Render

1. Sube este repositorio a GitHub
2. Crea cuenta en [Render](https://render.com)
3. New Web Service → Conecta GitHub
4. Configura:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Añade variable de entorno: `GROQ_API_KEY` (consíguela en console.groq.com)

## Integrar widget en tu web

Copia `chat-widget.js` y cambia `TU-APP-RENDER.onrender.com` por tu URL real