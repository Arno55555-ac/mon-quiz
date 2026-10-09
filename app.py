import streamlit as st
from mistralai.client import Mistral

st.title("💬 Mon chat avec mémoire")

client = Mistral(api_key=st.secrets["MISTRAL_API_KEY"])

# 1. Créer l'historique UNE seule fois (au premier chargement)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Bouton pour repartir de zéro
if st.button("🗑️ Nouvelle conversation"):
    st.session_state.messages = []
    st.rerun()

# 2. Réafficher tout l'historique à chaque rechargement de la page
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 3. Quand l'utilisateur envoie un nouveau message
question = st.chat_input("Écris ton message…")
if question:
    # On l'ajoute à l'historique et on l'affiche
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    # On envoie TOUT l'historique à Mistral, pas seulement la dernière question
    with st.chat_message("assistant"):
        with st.spinner("L'IA réfléchit…"):
            reponse = client.chat.complete(
                model="ministral-8b-latest",
                messages=st.session_state.messages,
            )
            texte = reponse.choices[0].message.content
        st.write(texte)

    # On garde aussi la réponse de l'IA dans l'historique
    st.session_state.messages.append({"role": "assistant", "content": texte})
