from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from config import EMBEDDING_MODEL,N_RESULTS


model = SentenceTransformer(EMBEDDING_MODEL)

def creer_index(chunks:list):
    embeddings = model.encode(chunks)
    embeddings_np = np.array(embeddings).astype('float32')
    index = faiss.IndexFlatL2(embeddings_np.shape[1])
    index.add(embeddings_np)
    return index,chunks

def rechercher(question:str,index,chunks:list):
    question_embedding = model.encode([question])
    question_np = np.array(question_embedding).astype('float32')
    distances, indices = index.search(question_np, k=N_RESULTS)
    chunks_pertinents = [chunks[i] for i in indices[0]]
    return chunks_pertinents


