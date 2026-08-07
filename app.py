import streamlit as st
from utils.rag import generer_reponse
from utils.pdf import decouper_en_chunk, lire_pdf
from utils.indexer import creer_index

st.set_page_config(
    page_title="DocBot",
    page_icon=":robot_face:",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Assistant intelligent pour vos documents PDF")
st.markdown("Téléversez un fichier PDF et posez vos questions pour obtenir des réponses basées sur le contenu du document.")

if "index" not in st.session_state:
    st.session_state.index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "messages" not in st.session_state:
    st.session_state.messages = []

pdf_upload = st.file_uploader("Téléversez un fichier PDF", type=["pdf"])

if pdf_upload is not None:
    if "index" not in st.session_state or st.session_state.get("pdf_nom") != pdf_upload.name:
        with st.spinner("Traitement du PDF et création de l'index..."):
            texte = lire_pdf(pdf_upload)
            chunks = decouper_en_chunk(texte)
            index, chunks_stockes = creer_index(chunks)
            st.session_state.index = index
            st.session_state.chunks = chunks_stockes
            st.session_state.pdf_nom = pdf_upload.name
            st.success("Index créé avec succès ! Vous pouvez maintenant poser vos questions.")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
        
    question = st.chat_input("Posez votre question ici...")

    if question:
        st.session_state.messages.append({"role": "user","content": question})

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("Recherche en cours..."):
                reponse, sources = generer_reponse(question, st.session_state.index, st.session_state.chunks)
            st.write(reponse)

        with st.expander("Sources utilisées"):
            for source in sources:
                st.markdown(f"- {source[:200]}...")
        st.session_state.messages.append({"role": "assistant", "content": reponse})

else:
    st.info("Commence par uploader un PDF")
