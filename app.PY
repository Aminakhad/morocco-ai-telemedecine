import streamlit as st

st.set_page_config(
    page_title="Morocco AI Telemedicine",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Morocco AI-Assisted Telemedicine")
st.subheader("Pré-consultation assistée par intelligence artificielle")

st.info(
    "Prototype de recherche pour l'étude de la télémédecine "
    "assistée par IA dans le contexte marocain."
)

st.divider()

st.header("👤 Informations du patient")

age = st.number_input(
    "Âge",
    min_value=0,
    max_value=120,
    value=30
)

sexe = st.selectbox(
    "Sexe",
    ["Femme", "Homme", "Préfère ne pas répondre"]
)

langue = st.selectbox(
    "Langue préférée",
    ["Français", "العربية"]
)

st.header("🩺 Motif de consultation")

symptomes = st.text_area(
    "Décrivez vos symptômes",
    placeholder="Exemple : fièvre, toux, douleur..."
)

duree = st.text_input(
    "Depuis combien de temps avez-vous ces symptômes ?"
)

if st.button("Continuer"):
    
    st.success("Informations enregistrées.")

    st.subheader("📋 Résumé de pré-consultation")

    st.write("**Âge :**", age)
    st.write("**Sexe :**", sexe)
    st.write("**Langue :**", langue)
    st.write("**Symptômes :**", symptomes)
    st.write("**Durée :**", duree)

    st.warning(
        "Dans la prochaine version, le module IA analysera "
        "les informations et préparera un résumé destiné au médecin."
    )