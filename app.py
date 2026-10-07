import streamlit as st

st.title("Mon quiz")
st.write("Choisis une réponse pour chaque question, puis clique sur « Voir mon score ».")

# Liste des questions : la question, les choix possibles et la bonne réponse
questions = [
    {
        "question": "Quelle destination pour les vacances d'octobre ?",
        "choix": ["Les sables", "Les Canaries", "Rester à Igny"],
        "reponse": "Les sables",
    },
    {
        "question": "Combien de temps ?",
        "choix": ["8 jours", "10 jours", "15 jours"],
        "reponse": "8 jours",
    },
    {
        "question": "Quel activités à faire ?",
        "choix": ["Surf", "Musée", "Balade"],
        "reponse": "Surf",
    },
    {
        "question": "Quelle jour partir ?",
        "choix": ["Vendredi", "Samedi", "Dimanche"],
        "reponse": "Vendredi",
    },
    {
        "question": "Prendre les combinaisons ?",
        "choix": ["oui", "non", "à voir"],
        "reponse": "oui",
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
            






