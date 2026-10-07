import streamlit as st

st.title("Mon quiz")
st.write("Choisis une réponse pour chaque question, puis clique sur « Voir mon score ».")

# Liste des questions : la question, les choix possibles et la bonne réponse
questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "choix": ["Lyon", "Paris", "Marseille"],
        "reponse": "Paris",
    },
    {
        "question": "Combien font 5 x 3 ?",
        "choix": ["8", "15", "53"],
        "reponse": "15",
    },
    {
        "question": "Quel langage utilise Streamlit ?",
        "choix": ["Python", "JavaScript", "PHP"],
        "reponse": "Python",
    },
    {
        "question": "Quelle planète est la plus proche du Soleil ?",
        "choix": ["Vénus", "Mars", "Mercure"],
        "reponse": "Mercure",
    },
    {
        "question": "Combien y a-t-il de jours dans une semaine ?",
        "choix": ["5", "7", "10"],
        "reponse": "7",
    },
]

# Affichage des questions avec st.radio
reponses_utilisateur = []
for i, q in enumerate(questions):
    choix = st.radio(
        f"Question {i + 1} : {q['question']}",
        q["choix"],
        index=None,       # aucune réponse cochée au départ
        key=f"question_{i}",
    )
    reponses_utilisateur.append(choix)

# Bouton pour calculer le score
if st.button("Voir mon score"):
    if None in reponses_utilisateur:
        st.warning("Réponds à toutes les questions avant de voir ton score.")
    else:
        score = 0
        for i, q in enumerate(questions):
            if reponses_utilisateur[i] == q["reponse"]:
                score += 1
                st.write(f"✅ Question {i + 1} : correct")
            else:
                st.write(f"❌ Question {i + 1} : la bonne réponse était {q['reponse']}")

        st.success(f"Ton score : {score} / {len(questions)}")
        if score == len(questions):
            st.balloons()
            






