import streamlit as st

# ---------- CONFIG GÉNÉRALE ----------
st.set_page_config(
    page_title="Portail questionnaires – Béatrice Millêtre",
    page_icon="🧠",
    layout="wide",
)

# ---------- TITRE & INTRO ----------
st.title("Portail des questionnaires en ligne")
st.write(
    """
Bienvenue sur le portail unique de mes questionnaires psychologiques et outils de bilan.  
Choisissez le questionnaire que vous souhaitez passer.
"""
)

# Un petit séparateur visuel
st.markdown("---")

# ---------- STYLES LÉGERS POUR LES CARTES ----------
card_css = """
<style>
.q-card {
    padding: 1.2rem 1.4rem;
    border-radius: 0.8rem;
    border: 1px solid #e0e0e0;
    margin-bottom: 1.2rem;
}
.q-card h3 {
    margin-top: 0;
    margin-bottom: 0.4rem;
}
.q-card p {
    margin-bottom: 0.8rem;
}
</style>
"""
st.markdown(card_css, unsafe_allow_html=True)

# ---------- SECTION : QUESTIONNAIRES ----------
st.header("🧪 Questionnaires à remplir")

col1, col2 = st.columns(2)

# --- AQ / EQ ---
with col1:
    st.markdown('<div class="q-card">', unsafe_allow_html=True)
    st.markdown("### Questionnaire AQ / EQ")
    st.write(
        """
Questionnaire combiné sur :
- les dimensions autistiques (AQ),
- les dimensions empathiques (EQ).

Permet de repérer certains profils de neurodivergence et la façon d’entrer en relation avec les autres.
        """
    )
    st.link_button(
        "Passer le questionnaire AQ / EQ",
        "https://aq-eq-test.streamlit.app/",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# --- Bilan HPE ---
with col2:
    st.markdown('<div class="q-card">', unsafe_allow_html=True)
    st.markdown("### Bilan HPE")
    st.write(
        """
Questionnaire d’orientation pour explorer un **fonctionnement Haut Potentiel Emotionnel (HPE)** :
intensité émotionnelle, réactivité, empathie, relation aux autres et au monde.
        """
    )
    st.link_button(
        "Passer le bilan HPE",
        "https://bilan-hpe-app.streamlit.app/",
    )
    st.markdown("</div>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

# --- Degré de conscience ---
with col3:
    st.markdown('<div class="q-card">', unsafe_allow_html=True)
    st.markdown("### Questionnaire Degré de conscience")
    st.write(
        """
Exploration de la **conscience de soi** :
fonctionnement interne, observation de ses pensées, émotions et comportements,
capacité de recul et de métacognition.
        """
    )
    st.link_button(
        "Passer le questionnaire Degré de conscience",
        "https://degre-conscience-app-a8mez4xamxm4mgtid8uyfw.streamlit.app/",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# --- Neurodivergence / Neurodev ---
with col4:
    st.markdown('<div class="q-card">', unsafe_allow_html=True)
    st.markdown("### Questionnaire Neurodivergence / Neurodéveloppement")
    st.write(
        """
Questionnaire de repérage des **profils neurodivergents** (HPI, HPE, TSA, TDAH, DYS, etc.),
centré sur le vécu au quotidien, les forces et les difficultés dans différents contextes
(vie personnelle, scolaire, professionnelle).
        """
    )
    st.link_button(
        "Passer le questionnaire Neurodivergence",
        "https://neurodev-36fumdvirmh9b4gaucl5pc.streamlit.app/",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- TROISIÈME LIGNE : Compétences sociales / ToM + Cohérence centrale ----------
col5, col6 = st.columns(2)

with col5:
    st.markdown('<div class="q-card">', unsafe_allow_html=True)
    st.markdown("### Questionnaire Compétences sociales / Théorie de l’esprit")
    st.write(
        """
Questionnaire pour adolescents et adultes évaluant :

- les compétences sociales (compréhension, communication, flexibilité, autonomie),
- la régulation émotionnelle en interaction,
- et un niveau global de **théorie de l’esprit (ToM)**.

Les résultats détaillés sont accessibles au praticien via un code anonyme.
        """
    )
    st.link_button(
        "Passer le questionnaire Compétences sociales",
        "https://theory-of-mind.streamlit.app/",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# --- Cohérence centrale ---
with col6:
    st.markdown('<div class="q-card">', unsafe_allow_html=True)
    st.markdown("### Questionnaire Cohérence centrale (ECC-24)")
    st.write(
        """
Questionnaire évaluant le **style de traitement de l’information** :

- préférence pour les détails ou pour la vision globale,
- capacité à intégrer les informations dans un ensemble cohérent,
- prise en compte du contexte,
- flexibilité entre focus local et vue d’ensemble.

Outil particulièrement utile en contexte TSA, HPI et profils neurodivergents.
        """
    )
    st.link_button(
        "Passer le questionnaire Cohérence centrale",
        "https://coherencecentrale.streamlit.app/",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- SECTION FUTURE : ESPACE PRATICIEN ----------
st.markdown("---")
st.header("🔐 Espace praticien (bientôt)")

st.info(
    """
Prochaines évolutions possibles :

- Accès praticien sécurisé par un code,
- Tableau de bord listant toutes les passations,
- Téléchargement des réponses en CSV,
- Accès aux rapports PDF.

Pour l’instant, utilisez ce portail uniquement pour orienter les patients vers les bons questionnaires.
"""
)
