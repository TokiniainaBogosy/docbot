from groq import Groq
from dotenv import load_dotenv
import os
from config import LLM_MODEL
from utils.indexer import rechercher

load_dotenv()
client_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generer_reponse(question, index, chunks):
    chunks_pertinents = rechercher(question, index, chunks)
    contexte = "\n".join([f"- {chunk}" for chunk in chunks_pertinents])
    reponse = client_groq.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": """Tu es un assistant général.
                    Réponds UNIQUEMENT en te basant sur les extraits fournis.
                    Si la réponse n'est pas dans le contexte, dis-le clairement.
                    Réponds en français, de manière concise."""
            },
            {
                "role": "user",
                "content": f"Contexte:\n{contexte}\n\nQuestion: {question}"
            }
        ]
    )
    return reponse.choices[0].message.content.strip() , chunks_pertinents