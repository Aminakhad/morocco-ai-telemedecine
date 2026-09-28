import streamlit as st

# =========================
# DOSSIER PATIENT PARTAGÉ
# =========================

if "dossier_patient" not in st.session_state:
    st.session_state.dossier_patient = None
# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Morocco AI-Assisted Telemedicine",
    page_icon="🩺",
    layout="wide"
)

# ============================================================
# CHOIX DE LA LANGUE
# ============================================================

langue = st.selectbox(
    "🌐 Langue / اللغة",
    ["Français", "العربية"]
)

arabe = langue == "العربية"

# ============================================================
# STYLE ARABE / FRANÇAIS
# ============================================================

if arabe:
    st.markdown(
        """
        <style>
        .stApp {
            direction: rtl;
        }

        .stMarkdown,
        .stTextInput,
        .stTextArea,
        .stSelectbox,
        .stNumberInput,
        .stSlider,
        .stCheckbox,
        .stButton,
        .stFileUploader {
            direction: rtl;
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            direction: ltr;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# TRADUCTIONS
# ============================================================

if arabe:

    T = {

        "title":
        "🩺 التطبيب عن بُعد بمساعدة الذكاء الاصطناعي",

        "subtitle":
        "نموذج أولي بحثي لدراسة دمج الذكاء الاصطناعي في خدمات التطبيب عن بُعد في المغرب.",

        "section1":
        "👤 1. المعلومات الاجتماعية والديموغرافية",

        "age":
        "العمر",

        "sex":
        "الجنس",

        "female":
        "أنثى",

        "male":
        "ذكر",

        "other":
        "آخر / أفضل عدم الإجابة",

        "region":
        "الجهة",

        "urban":
        "حضري",

        "rural":
        "قروي",

        "education":
        "المستوى التعليمي",

        "no_education":
        "بدون تعليم",

        "primary":
        "ابتدائي",

        "middle":
        "إعدادي",

        "high_school":
        "ثانوي",

        "bac2":
        "باك+2",

        "licence":
        "إجازة",

        "master":
        "ماستر",

        "doctorate":
        "دكتوراه",

        "profession":
        "المهنة / الوضع المهني",

        "digital":
        "مستوى الثقافة الرقمية الذاتية",

        "section2":
        "💻 2. الثقافة الرقمية والتطبيب عن بُعد",

        "internet":
        "هل لديك إمكانية الوصول إلى الإنترنت؟",

        "yes":
        "نعم",

        "no":
        "لا",

        "device":
        "الجهاز المستخدم عادة",

        "smartphone":
        "هاتف ذكي",

        "computer":
        "حاسوب",

        "tablet":
        "جهاز لوحي",

        "other_device":
        "آخر",

        "heard":
        "هل سمعت من قبل عن التطبيب عن بُعد؟",

        "used":
        "هل سبق لك استخدام خدمة للتطبيب عن بُعد؟",

        "section3":
        "🩺 3. معلومات الاستشارة الأولية",

        "reason":
        "سبب الاستشارة",

        "symptoms":
        "الأعراض",

        "duration":
        "مدة الأعراض",

        "intensity":
        "شدة الأعراض",

        "history":
        "السوابق المرضية",

        "medications":
        "الأدوية الحالية",

        "consent":
        "أوافق على استخدام هذه المعلومات لأغراض البحث.",

        "prepare":
        "🚀 تحضير الاستشارة الأولية",

        "prepared":
        "تم إعداد الاستشارة الأولية بنجاح.",

        "consent_warning":
        "يرجى تأكيد الموافقة قبل المتابعة.",

        "documents":
        "📎 الوثائق الطبية",

        "documents_description":
        "يمكنك تحميل التحاليل الطبية، الأشعة، تخطيط القلب ECG، السكانير، التصوير بالرنين المغناطيسي أو التقارير الطبية.",

        "upload":
        "تحميل وثيقة أو عدة وثائق طبية",

        "uploaded":
        "تم تحميل الوثيقة/الوثائق بنجاح.",

        "provided":
        "📋 الوثائق المقدمة",

        "document_warning":
        "⚠️ سيتم عرض الوثائق على المهني الصحي. هذه النسخة من النموذج الأولي لا تقوم بتفسير الصور الطبية ولا تقدم تشخيصاً.",

        "ai":
        "🤖 مساعد الذكاء الاصطناعي — محاكاة",

        "ai_description":
        "تحاكي هذه النسخة مساعداً ذكياً يقوم بتنظيم معلومات المريض وإعداد ملخص يساعد المهني الصحي على التحضير للاستشارة عن بُعد.",

        "analyze":
        "🚀 تحليل المعلومات بواسطة المساعد",

        "analysis":
        "🧠 التحليل المحاكى",

        "summary":
        "📋 الملخص المنظم للمريض",

        "clinical":
        "🩺 المعلومات السريرية",

        "missing":
        "⚠️ المعلومات التي يجب استكمالها",

        "available":
        "المعلومات الأساسية متوفرة.",

        "verify":
        "🔎 نقاط يجب التحقق منها من طرف المهني الصحي",

        "doctor":
        "👨‍⚕️ ملخص موجه إلى المهني الصحي",

        "documents_count":
        "عدد الوثائق الطبية المقدمة",

        "no_documents":
        "لم يتم تقديم أي وثيقة طبية.",

        "important":
        "⚠️ تنبيه",

        "safety":
        "هذا نموذج أولي بحثي. لا يقدم المساعد تشخيصاً طبياً ولا يحل محل قرار المهني الصحي."

    }

else:

    T = {

        "title":
        "🩺 Morocco AI-Assisted Telemedicine",

        "subtitle":
        "Prototype de recherche développé pour étudier l'intégration de l'intelligence artificielle dans la télémédecine au Maroc.",

        "section1":
        "👤 1. Informations sociodémographiques",

        "age":
        "Âge",

        "sex":
        "Sexe",

        "female":
        "Femme",

        "male":
        "Homme",

        "other":
        "Autre / préfère ne pas répondre",

        "region":
        "Région",

        "urban":
        "Urbain",

        "rural":
        "Rural",

        "education":
        "Niveau d'éducation",

        "no_education":
        "Sans instruction",

        "primary":
        "Primaire",

        "middle":
        "Collège",

        "high_school":
        "Lycée",

        "bac2":
        "Bac+2",

        "licence":
        "Licence",

        "master":
        "Master",

        "doctorate":
        "Doctorat",

        "profession":
        "Profession / situation professionnelle",

        "digital":
        "Littératie numérique (auto-évaluation)",

        "section2":
        "💻 2. Culture numérique et télémédecine",

        "internet":
        "Avez-vous accès à Internet ?",

        "yes":
        "Oui",

        "no":
        "Non",

        "device":
        "Appareil principalement utilisé",

        "smartphone":
        "Smartphone",

        "computer":
        "Ordinateur",

        "tablet":
        "Tablette",

        "other_device":
        "Autre",

        "heard":
        "Avez-vous déjà entendu parler de la télémédecine ?",

        "used":
        "Avez-vous déjà utilisé un service de télémédecine ?",

        "section3":
        "🩺 3. Informations de pré-consultation",

        "reason":
        "Motif de consultation",

        "symptoms":
        "Symptômes",

        "duration":
        "Durée des symptômes",

        "intensity":
        "Intensité des symptômes",

        "history":
        "Antécédents médicaux",

        "medications":
        "Médicaments actuels",

        "consent":
        "J'accepte l'utilisation de ces informations à des fins de recherche.",

        "prepare":
        "🚀 Préparer ma pré-consultation",

        "prepared":
        "La pré-consultation a été préparée avec succès.",

        "consent_warning":
        "Veuillez confirmer votre consentement avant de continuer.",

        "documents":
        "📎 Documents médicaux",

        "documents_description":
        "Vous pouvez importer vos analyses, radiographies, ECG, scanners, IRM ou comptes rendus médicaux.",

        "upload":
        "Importer un ou plusieurs documents médicaux",

        "uploaded":
        "Document(s) importé(s) avec succès.",

        "provided":
        "📋 Documents fournis",

        "document_warning":
        "⚠️ Les documents seront destinés à être examinés par le professionnel de santé. Cette version du prototype n'interprète pas les images médicales et ne fournit pas de diagnostic.",

        "ai":
        "🤖 Assistant IA — Simulation",

        "ai_description":
        "Cette version simule un assistant intelligent qui organise les informations du patient et prépare une synthèse destinée au professionnel de santé.",

        "analyze":
        "🚀 Analyser avec l'assistant IA",

        "analysis":
        "🧠 Analyse simulée",

        "summary":
        "📋 Résumé structuré du patient",

        "clinical":
        "🩺 Informations cliniques",

        "missing":
        "⚠️ Informations à compléter",

        "available":
        "Les informations principales sont disponibles.",

        "verify":
        "🔎 Points à vérifier par le professionnel",

        "doctor":
        "👨‍⚕️ Synthèse destinée au professionnel",

        "documents_count":
        "Nombre de documents médicaux fournis",

        "no_documents":
        "Aucun document médical fourni.",

        "important":
        "⚠️ Attention",

        "safety":
        "Prototype de recherche : cet assistant ne fournit pas de diagnostic médical et ne remplace pas le jugement du professionnel de santé."

    }

# ============================================================
# INTERFACE MÉDECIN
# ============================================================

def interface_medecin():

    st.title("👨‍⚕️ Espace professionnel de santé")

    st.info(
        "Tableau de bord de démonstration pour la consultation "
        "des dossiers préparés avec l'assistance IA."
    )

    patients = {
        "P001 — Patiente, 25 ans": {
            "age": 25,
            "sexe": "Femme",
            "region": "Drâa-Tafilalet",
            "milieu": "Urbain",
            "education": "Master",
            "motif": "Fatigue",
            "symptomes": "Maux de tête, fatigue, manque d'énergie",
            "duree": "3 mois",
            "intensite": 5,
            "antecedents": "Rien",
            "medicaments": "Rien",
            "documents": [
                "Document médical fourni par le patient"
            ],
            "questions": [
                "Depuis quand la fatigue est-elle présente ?",
                "Le sommeil est-il réparateur ?",
                "La fatigue empêche-t-elle les activités quotidiennes ?",
                "Existe-t-il d'autres symptômes associés ?"
            ],
            "synthese_ia": (
                "Patiente de 25 ans présentant une fatigue "
                "persistante associée à des maux de tête "
                "et un manque d'énergie depuis 3 mois. "
                "Intensité déclarée : 5/10."
            )
        }
    }

    patient_selectionne = st.selectbox(
        "📋 Sélectionner un dossier patient",
        list(patients.keys()),
        key="doctor_patient_selection"
    )

    patient = patients[patient_selectionne]

    st.divider()

    st.header("👤 Informations du patient")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(f"**Âge :** {patient['age']} ans")
        st.write(f"**Sexe :** {patient['sexe']}")

    with col2:
        st.write(f"**Région :** {patient['region']}")
        st.write(f"**Milieu :** {patient['milieu']}")

    with col3:
        st.write(f"**Éducation :** {patient['education']}")
        st.write(f"**Motif :** {patient['motif']}")

    st.header("🩺 Informations cliniques")

    st.write(f"**Symptômes :** {patient['symptomes']}")
    st.write(f"**Durée :** {patient['duree']}")
    st.write(f"**Intensité :** {patient['intensite']}/10")
    st.write(f"**Antécédents :** {patient['antecedents']}")
    st.write(f"**Médicaments :** {patient['medicaments']}")

    st.header("📎 Documents médicaux")

    for document in patient["documents"]:
        st.write("📄 " + document)

    st.header("❓ Questions complémentaires suggérées par l'IA")

    for question in patient["questions"]:
        st.write("• " + question)

    st.header("🤖 Synthèse générée par l'assistant IA")

    st.info(patient["synthese_ia"])

    st.header("👨‍⚕️ Validation professionnelle")

    synthese_medecin = st.text_area(
        "Synthèse validée / corrigée",
        value=patient["synthese_ia"],
        height=180,
        key="doctor_summary"
    )

    col4, col5 = st.columns(2)

    with col4:
        if st.button(
            "✅ Valider la synthèse",
            key="validate_doctor"
        ):
            st.success(
                "La synthèse a été validée par le professionnel."
            )

    with col5:
        if st.button(
            "✏️ Enregistrer une correction",
            key="correct_doctor"
        ):
            st.success(
                "La correction a été enregistrée dans le prototype."
            )

    st.header("📝 Note du professionnel")

    note_medecin = st.text_area(
        "Ajouter une note clinique",
        key="doctor_note"
    )

    if st.button(
        "💾 Enregistrer la note",
        key="save_doctor_note"
    ):
        st.success("Note enregistrée dans le prototype.")

    st.caption(
        "⚠️ Version de démonstration : les données affichées "
        "sont fictives."
    )
# =========================
    # DOSSIER TRANSMIS PAR LE PATIENT
    # =========================

    st.divider()
    st.header("📁 Dossier patient transmis")

    dossier = st.session_state.get("dossier_patient")

    if dossier is None:
        st.info("Aucun dossier patient n'a encore été transmis.")

    else:
        st.success("✅ Un dossier patient est disponible.")

        st.subheader("👤 Informations du patient")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**ID :**", dossier["ID"])
            st.write("**Âge :**", dossier["Âge"])
            st.write("**Sexe :**", dossier["Sexe"])
            st.write("**Région :**", dossier["Région"])

        with col2:
            st.write("**Milieu :**", dossier["Milieu"])
            st.write("**Niveau d'éducation :**", dossier["Niveau d'éducation"])
            st.write("**Profession :**", dossier["Profession"])

        st.subheader("🩺 Informations cliniques")

        st.write("**Motif :**", dossier["Motif"])
        st.write("**Symptômes :**", dossier["Symptômes"])
        st.write("**Durée :**", dossier["Durée"])
        st.write("**Intensité :**", dossier["Intensité"])
        st.write("**Antécédents :**", dossier["Antécédents"])
        st.write("**Médicaments :**", dossier["Médicaments"])

# ============================================================
# CHOIX PATIENT / PROFESSIONNEL
# ============================================================

type_utilisateur = st.radio(
    "👤 Type d'utilisateur",
    [
        "Patient",
        "Professionnel de santé"
    ],
    horizontal=True,
    key="user_type"
)

if type_utilisateur =="Professionnel de santé":
    interface_medecin()
    st.stop()

# =========================================================
# MODULE COMPLÉMENTAIRE — DOSSIER MÉDECIN
# =========================================================

if type_utilisateur == "Professionnel de santé":

    st.divider()

    st.header("📂 Dossier médical du patient")

    st.info(
        "Cet espace permet au professionnel de santé de consulter "
        "les informations préparées par le patient et l'assistant IA."
    )

    # ---------------------------------------------------------
    # 1. SÉLECTION DU PATIENT
    # ---------------------------------------------------------

    patient_selectionne = st.selectbox(
        "Sélectionner un dossier patient",
        [
            "P001 — Patiente, 25 ans",
            "P002 — Patient, 42 ans",
            "P003 — Patiente, 58 ans"
        ],
        key="doctor_patient_selection_module"
    )

    st.divider()

    # ---------------------------------------------------------
    # 2. INFORMATIONS DU PATIENT
    # ---------------------------------------------------------

    st.subheader("👤 Informations du patient")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Âge :** 25 ans")
        st.write("**Sexe :** Femme")
        st.write("**Région :** Drâa-Tafilalet")

    with col2:
        st.write("**Milieu :** Urbain")
        st.write("**Niveau d'éducation :** Master")
        st.write("**Littératie numérique :** 4/5")

    st.divider()

    # ---------------------------------------------------------
    # 3. INFORMATIONS CLINIQUES
    # ---------------------------------------------------------

    st.subheader("🩺 Informations cliniques")

    st.write("**Motif de consultation :** Fatigue")
    st.write("**Symptômes :** Maux de tête, fatigue, manque d'énergie")
    st.write("**Durée :** 3 mois")
    st.write("**Intensité déclarée :** 5/10")
    st.write("**Antécédents médicaux :** Aucun renseigné")
    st.write("**Médicaments actuels :** Aucun renseigné")

    st.divider()

    # ---------------------------------------------------------
    # 4. DOCUMENTS MÉDICAUX
    # ---------------------------------------------------------

    st.subheader("📎 Documents médicaux transmis")

    documents_patient = [
        "WhatsApp Image 2026-09-27 at 20.50.31.jpeg"
    ]

    if len(documents_patient) > 0:

        st.success(
            f"{len(documents_patient)} document(s) médical(aux) disponible(s)."
        )

        for document in documents_patient:
            st.write("📄", document)

    else:

        st.warning(
            "Aucun document médical n'a été transmis par le patient."
        )

    st.divider()

    # ---------------------------------------------------------
    # 5. SYNTHÈSE DE L'ASSISTANT IA
    # ---------------------------------------------------------

    st.subheader("🤖 Synthèse préparée par l'assistant IA")

    st.info(
        "L'assistant IA organise les informations fournies par le patient "
        "afin de faciliter la préparation de la consultation."
    )

    st.write("**Motif principal :** Fatigue")

    st.write(
        "**Informations rapportées :** fatigue persistante, "
        "maux de tête et manque d'énergie depuis environ 3 mois."
    )

    st.write(
        "**Informations complémentaires à vérifier :** qualité du sommeil, "
        "impact sur les activités quotidiennes, localisation et fréquence "
        "des maux de tête et présence éventuelle d'autres symptômes."
    )

    st.warning(
        "Cette synthèse constitue une aide à la consultation. "
        "Elle ne fournit pas de diagnostic et ne remplace pas "
        "le jugement du professionnel de santé."
    )

    st.divider()

    # ---------------------------------------------------------
    # 6. NOTES DU PROFESSIONNEL
    # ---------------------------------------------------------

    st.subheader("📝 Notes du professionnel de santé")

    notes_medecin = st.text_area(
        "Ajouter vos observations ou notes cliniques",
        placeholder="Écrire ici les observations du professionnel...",
        key="doctor_notes"
    )

    if st.button(
        "💾 Enregistrer les notes",
        key="save_doctor_notes"
    ):
        st.success("Les notes ont été enregistrées dans le prototype.")
       

# ============================================================
# TITRE
# ============================================================

st.title(T["title"])
st.info(T["subtitle"])

# ============================================================
# 1. INFORMATIONS SOCIODÉMOGRAPHIQUES
# ============================================================

st.header(T["section1"])

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        T["age"],
        min_value=18,
        max_value=100,
        value=30
    )

    sexe = st.selectbox(
        T["sex"],
        [
            T["female"],
            T["male"],
            T["other"]
        ]
    )

    if arabe:

        regions = [
            "درعة تافيلالت",
            "مراكش آسفي",
            "الرباط سلا القنيطرة",
            "الدار البيضاء سطات",
            "فاس مكناس",
            "طنجة تطوان الحسيمة",
            "سوس ماسة",
            "الشرق",
            "بني ملال خنيفرة",
            "كلميم واد نون",
            "العيون الساقية الحمراء",
            "الداخلة وادي الذهب"
        ]

    else:

        regions = [
            "Drâa-Tafilalet",
            "Marrakech-Safi",
            "Rabat-Salé-Kénitra",
            "Casablanca-Settat",
            "Fès-Meknès",
            "Tanger-Tétouan-Al Hoceïma",
            "Souss-Massa",
            "Oriental",
            "Béni Mellal-Khénifra",
            "Guelmim-Oued Noun",
            "Laâyoune-Sakia El Hamra",
            "Dakhla-Oued Ed-Dahab"
        ]

    region = st.selectbox(
        T["region"],
        regions
    )

    milieu = st.selectbox(
        T["region"] if False else "الوسط" if arabe else "Milieu",
        [
            T["urban"],
            T["rural"]
        ]
    )

with col2:

    education = st.selectbox(
        T["education"],
        [
            T["no_education"],
            T["primary"],
            T["middle"],
            T["high_school"],
            T["bac2"],
            T["licence"],
            T["master"],
            T["doctorate"]
        ]
    )

    profession = st.text_input(
        T["profession"]
    )

    litteratie = st.slider(
        T["digital"],
        min_value=1,
        max_value=5,
        value=3
    )

# ============================================================
# 2. CULTURE NUMÉRIQUE ET TÉLÉMÉDECINE
# ============================================================

st.header(T["section2"])

col3, col4 = st.columns(2)

with col3:

    internet = st.selectbox(
        T["internet"],
        [
            T["yes"],
            T["no"]
        ]
    )

    device = st.selectbox(
        T["device"],
        [
            T["smartphone"],
            T["computer"],
            T["tablet"],
            T["other_device"]
        ]
    )

with col4:

    awareness = st.selectbox(
        T["heard"],
        [
            T["yes"],
            T["no"]
        ]
    )

    telemedicine_use = st.selectbox(
        T["used"],
        [
            T["yes"],
            T["no"]
        ]
    )

# ============================================================
# 3. INFORMATIONS DE PRÉ-CONSULTATION
# ============================================================

st.header(T["section3"])

motif = st.text_input(
    T["reason"]
)

symptomes = st.text_area(
    T["symptoms"]
)

duree = st.text_input(
    T["duration"]
)

intensite = st.slider(
    T["intensity"],
    min_value=0,
    max_value=10,
    value=5
)

antecedents = st.text_area(
    T["history"]
)

medicaments = st.text_area(
    T["medications"]
)

consent = st.checkbox(
    T["consent"]
)

# ============================================================
# PRÉPARER LA PRÉ-CONSULTATION
# ============================================================

if st.button(T["prepare"]):

    if not consent:

        st.warning(
            T["consent_warning"]
        )

    else:

        st.success(
            T["prepared"]
        )

# ============================================================
# 4. DOCUMENTS MÉDICAUX
# ============================================================

st.divider()

st.header(T["documents"])

st.write(
    T["documents_description"]
)

documents = st.file_uploader(
    T["upload"],
    type=[
        "pdf",
        "png",
        "jpg",
        "jpeg",
        "dcm"
    ],
    accept_multiple_files=True
)

if documents:

    st.success(
        f"{T['uploaded']} : {len(documents)}"
    )

    st.subheader(
        T["provided"]
    )

    for document in documents:

        taille = document.size / 1024

        st.write(
            f"📄 **{document.name}** — {taille:.1f} Ko"
        )

else:

    st.info(
        T["no_documents"]
    )

st.warning(
    T["document_warning"]
)

# ============================================================
# 5. ASSISTANT IA — SIMULATION
# ============================================================

st.divider()

st.header(T["ai"])

st.write(
    T["ai_description"]
)

if st.button(T["analyze"]):

    # ----------------------------------------
    # Informations manquantes
    # ----------------------------------------

    informations_manquantes = []

    if not motif:
        informations_manquantes.append(
            T["reason"]
        )

    if not symptomes:
        informations_manquantes.append(
            T["symptoms"]
        )

    if not duree:
        informations_manquantes.append(
            T["duration"]
        )

    if not antecedents:
        informations_manquantes.append(
            T["history"]
        )

    if not medicaments:
        informations_manquantes.append(
            T["medications"]
        )

    # ----------------------------------------
    # ANALYSE
    # ----------------------------------------

    st.subheader(
        T["analysis"]
    )

    # ----------------------------------------
    # RÉSUMÉ STRUCTURÉ
    # ----------------------------------------

    st.subheader(
        T["summary"]
    )

    st.write(
        f"**{T['age']} :** {age}"
    )

    st.write(
        f"**{T['sex']} :** {sexe}"
    )

    st.write(
        f"**{T['region']} :** {region}"
    )

    st.write(
        f"**{T['education']} :** {education}"
    )

    st.write(
        f"**{T['digital']} :** {litteratie}/5"
    )

    st.write(
        f"**{T['reason']} :** {motif}"
    )

    st.write(
        f"**{T['symptoms']} :** {symptomes}"
    )

    st.write(
        f"**{T['duration']} :** {duree}"
    )

    st.write(
        f"**{T['intensity']} :** {intensite}/10"
    )

    st.write(
        f"**{T['history']} :** {antecedents}"
    )

    st.write(
        f"**{T['medications']} :** {medicaments}"
    )

    # ----------------------------------------
    # DOCUMENTS
    # ----------------------------------------

    st.markdown("---")

    if documents:

        st.write(
            f"📎 **{T['documents_count']} :** {len(documents)}"
        )

        for document in documents:

            st.write(
                f"• {document.name}"
            )

    else:

        st.write(
            f"📎 **{T['documents_count']} :** 0"
        )

    # ----------------------------------------
    # INFORMATIONS MANQUANTES
    # ----------------------------------------

    st.subheader(
        T["missing"]
    )

    if informations_manquantes:

        for information in informations_manquantes:

            st.warning(
                information
            )

    else:

        st.success(
            T["available"]
        )

    # ----------------------------------------
    # POINTS À VÉRIFIER
    # ----------------------------------------

    st.subheader(
        T["verify"]
    )

    if arabe:

        st.info(
            "يجب على المهني الصحي التحقق من تطور الأعراض، "
            "السوابق المرضية، الأدوية الحالية، والمعلومات "
            "الواردة في الوثائق الطبية قبل اتخاذ أي قرار."
        )

    else:

        st.info(
            "Le professionnel de santé doit vérifier "
            "l'évolution des symptômes, les antécédents, "
            "les traitements actuels et les documents médicaux "
            "avant toute décision."
        )

    # ----------------------------------------
    # SYNTHÈSE POUR LE PROFESSIONNEL
    # ----------------------------------------

    st.subheader(
        T["doctor"]
    )

    if arabe:

        st.success(
            "قام المريض بإكمال الاستشارة الأولية. "
            "تم تنظيم المعلومات المتوفرة والوثائق المقدمة "
            "لتسهيل التحضير للاستشارة عن بُعد."
        )

    else:

        st.success(
            "Le patient a complété une pré-consultation. "
            "Les informations disponibles et les documents "
            "fournis ont été structurés afin de faciliter "
            "la préparation de la téléconsultation."
        )

    # ----------------------------------------
    # SÉCURITÉ
    # ----------------------------------------

    st.caption(
        T["safety"]
    )
# =========================================================
# TRANSMISSION DU DOSSIER AU PROFESSIONNEL
# =========================================================

st.divider()

st.subheader("📤 Transmission au professionnel de santé")

st.write(
    "Après avoir vérifié vos informations, vous pouvez transmettre "
    "votre dossier au professionnel de santé."
)

if st.button(
    "📤 Envoyer mon dossier au professionnel de santé",
    key="send_patient_file"
):

    st.session_state.dossier_patient = {
        "ID": "P001",
        "Âge": age,
        "Sexe": sexe,
        "Région": region,
        "Milieu": milieu,
        "Niveau d'éducation": education,
        "Profession": profession,
        "Littératie numérique": litteratie,
        "Motif": motif,
        "Symptômes": symptomes,
        "Durée": duree,
        "Intensité": intensite,
        "Antécédents": antecedents,
        "Médicaments": medicaments
    }

    st.success(
        "✅ Votre dossier a été transmis au professionnel de santé."
    )
# ============================================================
# 5. ASSISTANT IA — SIMULATION INTELLIGENTE
# ============================================================

def analyser_symptomes(symptomes, motif, intensite):

    texte = (
        str(motif) + " " + str(symptomes)
    ).lower()

    analyse = {
        "categories": [],
        "points_attention": [],
        "questions": [],
        "priorite": "Évaluation clinique standard"
    }

    # --------------------------------------------------------
    # Catégories de symptômes
    # --------------------------------------------------------

    if any(
        mot in texte
        for mot in [
            "fatigue",
            "fatigué",
            "fatiguée",
            "énergie",
            "epuisement",
            "épuisement"
        ]
    ):
        analyse["categories"].append(
            "Fatigue / baisse d'énergie"
        )

        analyse["questions"].extend([
            "Depuis quand la fatigue est-elle présente ?",
            "Le sommeil est-il réparateur ?",
            "La fatigue empêche-t-elle les activités quotidiennes ?",
            "Existe-t-il d'autres symptômes associés ?"
        ])

    if any(
        mot in texte
        for mot in [
            "tête",
            "tete",
            "céphalée",
            "cephalee",
            "migraine"
        ]
    ):
        analyse["categories"].append(
            "Symptômes céphaliques"
        )

        analyse["questions"].extend([
            "Où se situe la douleur ?",
            "À quelle fréquence apparaît-elle ?",
            "Est-elle nouvelle ou habituelle ?",
            "Existe-t-il des troubles visuels, vomissements ou autres symptômes associés ?"
        ])

    if any(
        mot in texte
        for mot in [
            "douleur",
            "mal",
            "douleurs"
        ]
    ):
        analyse["categories"].append(
            "Douleur"
        )

        analyse["questions"].extend([
            "Où se situe la douleur ?",
            "Depuis quand est-elle présente ?",
            "Est-elle continue ou intermittente ?",
            "Qu'est-ce qui augmente ou diminue la douleur ?"
        ])

    if any(
        mot in texte
        for mot in [
            "fièvre",
            "fievre",
            "temperature",
            "température"
        ]
    ):
        analyse["categories"].append(
            "Fièvre / température élevée"
        )

        analyse["questions"].extend([
            "Quelle température maximale a été mesurée ?",
            "Depuis combien de temps ?",
            "Existe-t-il d'autres symptômes associés ?"
        ])

    if any(
        mot in texte
        for mot in [
            "toux",
            "respiration",
            "essoufflement",
            "dyspnée",
            "dyspnee"
        ]
    ):
        analyse["categories"].append(
            "Symptômes respiratoires"
        )

        analyse["questions"].extend([
            "Depuis combien de temps les symptômes sont-ils présents ?",
            "Existe-t-il une difficulté à respirer ?",
            "Les symptômes apparaissent-ils au repos ou à l'effort ?"
        ])

    if any(
        mot in texte
        for mot in [
            "ventre",
            "abdominal",
            "abdomen",
            "nausée",
            "nausées",
            "vomissement",
            "vomissements"
        ]
    ):
        analyse["categories"].append(
            "Symptômes digestifs / abdominaux"
        )

        analyse["questions"].extend([
            "Où se situe exactement la douleur ou la gêne ?",
            "Existe-t-il des nausées ou vomissements ?",
            "Existe-t-il une modification du transit ?"
        ])

    # --------------------------------------------------------
    # Signaux nécessitant une vérification rapide
    # --------------------------------------------------------

    signaux_attention = [
        "douleur thoracique",
        "douleur poitrine",
        "difficulté à respirer",
        "difficulte a respirer",
        "perte de connaissance",
        "inconscient",
        "convulsion",
        "paralysie",
        "faiblesse d'un côté",
        "trouble de la parole",
        "saignement important",
        "hémorragie",
        "hemorragie"
    ]

    signaux_detectes = []

    for signal in signaux_attention:

        if signal in texte:
            signaux_detectes.append(signal)

    if signaux_detectes:

        analyse["priorite"] = (
            "Vérification clinique prioritaire"
        )

        analyse["points_attention"].append(
            "Certains éléments rapportés nécessitent "
            "une évaluation clinique rapide par un professionnel."
        )

    elif intensite >= 8:

        analyse["priorite"] = (
            "Évaluation clinique à prioriser"
        )

        analyse["points_attention"].append(
            "L'intensité déclarée des symptômes est élevée "
            "et doit être vérifiée par le professionnel."
        )

    else:

        analyse["priorite"] = (
            "Évaluation clinique standard"
        )

    # --------------------------------------------------------
    # Éviter les doublons
    # --------------------------------------------------------

    analyse["categories"] = list(
        dict.fromkeys(analyse["categories"])
    )

    analyse["questions"] = list(
        dict.fromkeys(analyse["questions"])
    )

    return analyse


# ============================================================
# INTERFACE ASSISTANT
# ============================================================

st.divider()

st.header(T["ai"])

st.write(
    T["ai_description"]
)

if st.button(T["analyze"],
key="ai_analysis_button"):

    # --------------------------------------------------------
    # Analyse simulée
    # --------------------------------------------------------

    resultat = analyser_symptomes(
        symptomes,
        motif,
        intensite
    )

    # --------------------------------------------------------
    # Informations manquantes
    # --------------------------------------------------------

    informations_manquantes = []

    if not motif:
        informations_manquantes.append(
            T["reason"]
        )

    if not symptomes:
        informations_manquantes.append(
            T["symptoms"]
        )

    if not duree:
        informations_manquantes.append(
            T["duration"]
        )

    if not antecedents:
        informations_manquantes.append(
            T["history"]
        )

    if not medicaments:
        informations_manquantes.append(
            T["medications"]
        )

    # ========================================================
    # ANALYSE
    # ========================================================

    st.subheader(
        T["analysis"]
    )

    # --------------------------------------------------------
    # Catégories détectées
    # --------------------------------------------------------

    if arabe:

        st.markdown("### 🧠 العناصر التي تم تحديدها")

        if resultat["categories"]:

            for categorie in resultat["categories"]:
                st.write("• " + categorie)

        else:

            st.write(
                "لم يتم تحديد فئة محددة للأعراض."
            )

    else:

        st.markdown("### 🧠 Éléments identifiés")

        if resultat["categories"]:

            for categorie in resultat["categories"]:
                st.write("• " + categorie)

        else:

            st.write(
                "Aucune catégorie spécifique identifiée."
            )

    # --------------------------------------------------------
    # Niveau de vérification
    # --------------------------------------------------------

    if arabe:

        st.markdown("### 🚦 Niveau de vérification")

        if resultat["priorite"] == "Vérification clinique prioritaire":

            st.error(
                "⚠️ بعض العناصر المذكورة تتطلب تقييماً "
                "سريرياً سريعاً من طرف مهني صحي."
            )

        elif resultat["priorite"] == "Évaluation clinique à prioriser":

            st.warning(
                "⚠️ شدة الأعراض المصرح بها مرتفعة "
                "ويجب التحقق منها من طرف المهني الصحي."
            )

        else:

            st.info(
                "التقييم السريري المعتاد."
            )

    else:

        st.markdown("### 🚦 Niveau de vérification")

        if resultat["priorite"] == "Vérification clinique prioritaire":

            st.error(
                "⚠️ Certains éléments rapportés nécessitent "
                "une évaluation clinique rapide par un professionnel."
            )

        elif resultat["priorite"] == "Évaluation clinique à prioriser":

            st.warning(
                "⚠️ L'intensité déclarée est élevée et "
                "doit être vérifiée par le professionnel."
            )

        else:

            st.info(
                "Évaluation clinique standard."
            )

    # ========================================================
    # QUESTIONS COMPLÉMENTAIRES
    # ========================================================

    if arabe:

        st.subheader(
            "❓ Questions complémentaires suggérées"
        )

        if resultat["questions"]:

            for question in resultat["questions"]:
                st.write("• " + question)

        else:

            st.write(
                "Aucune question complémentaire spécifique."
            )

    else:

        st.subheader(
            "❓ Questions complémentaires suggérées"
        )

        if resultat["questions"]:

            for question in resultat["questions"]:
                st.write("• " + question)

        else:

            st.write(
                "Aucune question complémentaire spécifique."
            )

    # ========================================================
    # RÉSUMÉ STRUCTURÉ
    # ========================================================

    st.subheader(
        T["summary"]
    )

    st.write(
        f"**{T['age']} :** {age}"
    )

    st.write(
        f"**{T['sex']} :** {sexe}"
    )

    st.write(
        f"**{T['region']} :** {region}"
    )

    st.write(
        f"**{T['education']} :** {education}"
    )

    st.write(
        f"**{T['digital']} :** {litteratie}/5"
    )

    st.markdown("---")

    st.subheader(
        T["clinical"]
    )

    st.write(
        f"**{T['reason']} :** {motif}"
    )

    st.write(
        f"**{T['symptoms']} :** {symptomes}"
    )

    st.write(
        f"**{T['duration']} :** {duree}"
    )

    st.write(
        f"**{T['intensity']} :** {intensite}/10"
    )

    st.write(
        f"**{T['history']} :** {antecedents}"
    )

    st.write(
        f"**{T['medications']} :** {medicaments}"
    )

    # ========================================================
    # DOCUMENTS
    # ========================================================

    st.markdown("---")

    if documents:

        if arabe:

            st.write(
                f"📎 عدد الوثائق الطبية المقدمة: {len(documents)}"
            )

        else:

            st.write(
                f"📎 **Nombre de documents médicaux fournis :** "
                f"{len(documents)}"
            )

        for document in documents:

            st.write(
                f"• {document.name}"
            )

    else:

        st.write(
            f"📎 {T['no_documents']}"
        )

    # ========================================================
    # INFORMATIONS MANQUANTES
    # ========================================================

    st.subheader(
        T["missing"]
    )

    if informations_manquantes:

        for information in informations_manquantes:

            st.warning(
                information
            )

    else:

        st.success(
            T["available"]
        )

    # ========================================================
    # SYNTHÈSE PROFESSIONNELLE
    # ========================================================

    st.subheader(
        T["doctor"]
    )

    if arabe:

        st.success(
            f"المريض يبلغ من العمر {age} سنة، "
            f"وقد صرح بـ: {motif}. "
            f"الأعراض المبلغ عنها: {symptomes}. "
            f"مدة الأعراض: {duree}. "
            f"شدة الأعراض المصرح بها: {intensite}/10. "
            f"تم تقديم {len(documents) if documents else 0} "
            f"وثيقة طبية."
        )

    else:

        st.success(
            f"Patient âgé de {age} ans. "
            f"Motif rapporté : {motif}. "
            f"Symptômes rapportés : {symptomes}. "
            f"Durée : {duree}. "
            f"Intensité déclarée : {intensite}/10. "
            f"Nombre de documents médicaux fournis : "
            f"{len(documents) if documents else 0}."
        )

    # ========================================================
    # SÉCURITÉ
    # ========================================================

    st.caption(
        T["safety"]
    )