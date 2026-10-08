import streamlit as st
from mistralai.client import Mistral

st.title("Ma première question à l'IA 🤖")

client = Mistral(api_key=st.secrets["MISTRAL_API_KEY"])

question = st.text_input("Pose ta question :")

if st.button("Envoyer"):
    if question:
        with st.spinner("L'IA réfléchit..."):
            reponse = client.chat.complete(
                model="ministral-8b-latest",
                messages=[{"role": "user", "content": question}],
            )
        st.write(reponse.choices[0].message.content)
    else:
        st.warning("Écris d'abord une question !")
        
        