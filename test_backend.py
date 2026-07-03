from utils.pdf import lire_pdf,decouper_en_chunk
from utils.indexer import creer_index
from utils.rag import generer_reponse

print("Lecture du PDF...")
texte = lire_pdf("lettre_motivation_stage_dev_web.pdf")
print(f"Texte extrait : {len(texte)} caractères\n")

chunks = decouper_en_chunk(texte)
print(f"Nombre de chunks : {len(chunks)}")

print("Indexation ")
index,chunk= creer_index(chunks)
print("Indexation terminée\n")

questions = [
    "Quel est l'objet de cette lettre ?",
    "Quelles sont les compétences mentionnées ?",
    "Quel poste est visé ?",
    "Pourquoi le candidat est-il motivé ?"
]

print("--- Questions sur le PDF ---\n")
for question in questions:
    print(f"Question : {question}")
    reponse, sources = generer_reponse(question, index, chunk)
    print(f"Réponse  : {reponse}")
    print(f"Sources  : {len(sources)} chunks utilisés")
    print("-" * 50)