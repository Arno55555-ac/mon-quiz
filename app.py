import streamlit as st
from mistralai.client import Mistral

st.title("💬 Mon chat avec mémoire")

# --- Protection par mot de passe (séance 19) ---
mot_de_passe = st.text_input("Mot de passe", type="password")
if mot_de_passe != st.secrets["APP_PASSWORD"]:
    if mot_de_passe:  # on n'affiche l'erreur que si quelque chose a été tapé
        st.error("Mot de passe incorrect")
    st.stop()  # on arrête tout ici : le chat ne s'affiche pas
# ------------------------------------------------

client = Mistral(api_key=st.secrets["MISTRAL_API_KEY"])

# --- Personnalités de l'IA (séance 20) ---
# Chaque consigne précise : le rôle, le ton, la langue.
PERSONNALITES = {
    "Professeur patient": (
        "Tu es un professeur bienveillant et patient. "
        "Tu expliques simplement, avec des exemples concrets, "
        "et tu vérifies que la personne a compris. "
        "Tu réponds toujours en français."
    ),
    "Chef cuisinier enthousiaste": (
        "Tu es un chef cuisinier français plein d'enthousiasme. "
        "Tu ramènes volontiers la conversation à la cuisine "
        "et tu donnes des astuces pratiques. "
        "Tu réponds toujours en français, avec bonne humeur."
    ),
    "Assistant très bref": (
        "Tu es un assistant efficace. "
        "Tu réponds en trois phrases maximum, sans détour. "
        "Tu réponds toujours en français."
    ),
}

choix = st.selectbox("Personnalité de l'IA", list(PERSONNALITES.keys()))
consigne = PERSONNALITES[choix]
# -----------------------------------------

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
                # La consigne passe en premier, puis toute la conversation
                messages=[{"role": "system", "content": consigne}]
                + st.session_state.messages,
            )
            texte = reponse.choices[0].message.content
        st.write(texte)

    # On garde aussi la réponse de l'IA dans l'historique
    st.session_state.messages.append({"role": "assistant", "content": texte})
