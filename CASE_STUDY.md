# Étude de cas — DocBot

## Contexte

Les entreprises accumulent des documents internes — manuels, procédures, 
contrats, fiches produits — que leurs employés peinent à exploiter. 
Trouver une information précise dans un PDF de 50 pages peut prendre 
15 à 30 minutes. Multiplié par des dizaines de recherches par semaine, 
c'est des heures perdues en productivité.

## Solution

DocBot est un assistant documentaire intelligent construit avec Python et 
l'IA générative. L'utilisateur uploade ses PDFs, pose ses questions en 
langage naturel, et obtient une réponse précise en quelques secondes — 
avec les sources correspondantes.

Pas d'installation, pas de formation. Une interface web accessible 
depuis n'importe quel navigateur.

## Résultats concrets

- Recherche d'information : de 15-30 minutes à moins de 10 secondes
- Disponible 24h/24, 7j/7, sans mobiliser un collègue
- Réponses sourcées — l'utilisateur peut vérifier l'origine de chaque info
- Déployable en moins d'une semaine sur n'importe quelle base documentaire

## Cas d'usage typiques

- PME : interroger manuels internes et procédures RH
- Cabinets : recherche rapide dans des contrats et documents juridiques
- E-commerce : support client automatisé sur fiches produits et CGV
- Écoles : assistant pédagogique sur cours et supports de formation

## Stack technique

Python · Streamlit · FAISS · Sentence Transformers · Groq API (LLM)

## Démo live

https://docbot-toky.streamlit.app/