from pypdf import PdfReader
from config import CHUNK_OVERLAP,CHUNK_SIZE


def lire_pdf(fichier):
    reader = PdfReader(fichier)
    texte = ""
    for page in reader.pages:
        texte += page.extract_text()
    return texte

def decouper_en_chunk(texte):
    chunks = []

    debut = 0
    while debut < len(texte):
        chunk = texte[debut:debut+CHUNK_SIZE]
        if chunk.strip():
            chunks.append(chunk)
        debut += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks

