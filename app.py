import streamlit as st
import re
from groq import Groq

# ================== CONFIGURATION ==================
st.set_page_config(
    page_title="ICPC Practice Arena | GlobalInternet.py",
    page_icon="🏆",
    layout="wide"
)

# Language texts
TEXTS = {
    "English": {
        "title": "🏆 ICPC Challenge Practice Arena",
        "subtitle": "Master algorithmic problem‑solving with AI coaching",
        "video_tab": "🎬 Video Introduction",
        "practice_tab": "📝 Practice Problem",
        "ai_tab": "🤖 AI Coach",
        "video_title": "Watch the full introduction video",
        "video_desc": "This video explains how to use the practice arena and how the AI coach works.",
        "video_placeholder": "Paste your Dropbox or YouTube video link (use ?dl=1 for Dropbox)",
        "problem_title": "Longest Increasing Subsequence (LIS)",
        "problem_statement": """Given an array of integers, find the length of the longest strictly increasing subsequence.

**Example:**  
Input: `[10, 9, 2, 5, 3, 7, 101, 18]`  
Output: `4` (the subsequence `[2, 3, 7, 101]` or `[2, 5, 7, 101]`)  

**Constraints:** n up to 10⁵, values up to 10⁹.  
Optimal solution runs in **O(n log n)** using patience sorting.""",
        "test_input": "Enter an array (comma‑separated):",
        "run_button": "Run & Check Solution",
        "result_correct": "✅ Correct! The length of the LIS is **{}**.",
        "result_wrong": "❌ Your code returned {}, but the correct length is {}. Debug with AI Coach.",
        "hint_placeholder": "Paste your code or describe your algorithm idea...",
        "hint_button": "Get AI Feedback",
        "ai_thinking": "AI is analyzing your approach...",
        "ai_error": "AI error: {}",
        "sidebar_howto": "How to use",
        "howto_list": ["Watch the video intro", "Solve the practice problem", "Ask AI Coach for hints", "Compete in ICPC 2025!"],
        "footer": "© 2026 GlobalInternet.py – Built for ICPC 2025 Online Winter Challenge",
        "security_badge": "🔐 End‑to‑end encryption active",
        "security_caption": "All data is secured and anonymized",
        "price_title": "Our Services",
        "price_list": [
            "Full source code – $499 USD",
            "Source + customization – $1,499 USD",
            "Enterprise plan – $2,999 USD"
        ]
    },
    "Français": {
        "title": "🏆 Arène d'entraînement ICPC",
        "subtitle": "Maîtrisez la résolution algorithmique avec un coach IA",
        "video_tab": "🎬 Introduction vidéo",
        "practice_tab": "📝 Problème pratique",
        "ai_tab": "🤖 Coach IA",
        "video_title": "Regardez la vidéo d'introduction complète",
        "video_desc": "Cette vidéo explique comment utiliser l'arène et comment le coach IA fonctionne.",
        "video_placeholder": "Collez votre lien Dropbox ou YouTube (utilisez ?dl=1 pour Dropbox)",
        "problem_title": "Plus longue sous‑séquence strictement croissante (LIS)",
        "problem_statement": """Soit un tableau d'entiers, trouvez la longueur de la plus longue sous‑séquence strictement croissante.

**Exemple :**  
Entrée : `[10, 9, 2, 5, 3, 7, 101, 18]`  
Sortie : `4` (la sous‑séquence `[2, 3, 7, 101]` ou `[2, 5, 7, 101]`)  

**Contraintes :** n jusqu'à 10⁵, valeurs jusqu'à 10⁹.  
La solution optimale s'exécute en **O(n log n)** avec le tri par patience.""",
        "test_input": "Entrez un tableau (séparé par des virgules) :",
        "run_button": "Exécuter et vérifier",
        "result_correct": "✅ Correct ! La longueur de la LIS est **{}**.",
        "result_wrong": "❌ Votre code a retourné {}, mais la bonne longueur est {}. Utilisez le Coach IA.",
        "hint_placeholder": "Collez votre code ou décrivez votre idée d'algorithme...",
        "hint_button": "Obtenir un feedback IA",
        "ai_thinking": "L'IA analyse votre approche...",
        "ai_error": "Erreur IA : {}",
        "sidebar_howto": "Comment utiliser",
        "howto_list": ["Regardez l'intro vidéo", "Résolvez le problème pratique", "Demandez des indices au coach IA", "Participez à l'ICPC 2025 !"],
        "footer": "© 2026 GlobalInternet.py – Conçu pour l'ICPC 2025 Online Winter Challenge",
        "security_badge": "🔐 Chiffrement de bout en bout actif",
        "security_caption": "Toutes les données sont sécurisées et anonymisées",
        "price_title": "Nos services",
        "price_list": [
            "Code source complet – 499 USD",
            "Code + personnalisation – 1 499 USD",
            "Formule Entreprise – 2 999 USD"
        ]
    },
    "Español": {
        "title": "🏆 Arena de práctica ICPC",
        "subtitle": "Domina la resolución algorítmica con un entrenador IA",
        "video_tab": "🎬 Introducción en video",
        "practice_tab": "📝 Problema práctico",
        "ai_tab": "🤖 Entrenador IA",
        "video_title": "Vea el video de introducción completo",
        "video_desc": "Este video explica cómo usar el área de práctica y cómo funciona el entrenador IA.",
        "video_placeholder": "Pegue su enlace de Dropbox o YouTube (use ?dl=1 para Dropbox)",
        "problem_title": "Subsecuencia creciente más larga (LIS)",
        "problem_statement": """Dado un arreglo de enteros, encuentre la longitud de la subsecuencia estrictamente creciente más larga.

**Ejemplo:**  
Entrada: `[10, 9, 2, 5, 3, 7, 101, 18]`  
Salida: `4` (la subsecuencia `[2, 3, 7, 101]` o `[2, 5, 7, 101]`)  

**Restricciones:** n hasta 10⁵, valores hasta 10⁹.  
La solución óptima se ejecuta en **O(n log n)** mediante ordenamiento por paciencia.""",
        "test_input": "Ingrese un arreglo (separado por comas):",
        "run_button": "Ejecutar y verificar",
        "result_correct": "✅ ¡Correcto! La longitud de la LIS es **{}**.",
        "result_wrong": "❌ Su código devolvió {}, pero la longitud correcta es {}. Use el Entrenador IA.",
        "hint_placeholder": "Pegue su código o describa su idea algorítmica...",
        "hint_button": "Obtener retroalimentación IA",
        "ai_thinking": "La IA está analizando su enfoque...",
        "ai_error": "Error IA: {}",
        "sidebar_howto": "Cómo usar",
        "howto_list": ["Vea la introducción en video", "Resuelva el problema práctico", "Pida pistas al entrenador IA", "¡Participe en ICPC 2025!"],
        "footer": "© 2026 GlobalInternet.py – Creado para el ICPC 2025 Online Winter Challenge",
        "security_badge": "🔐 Cifrado de extremo a extremo activo",
        "security_caption": "Todos los datos están seguros y anonimizados",
        "price_title": "Nuestros servicios",
        "price_list": [
            "Código fuente completo – $499 USD",
            "Código + personalización – $1,499 USD",
            "Plan Empresarial – $2,999 USD"
        ]
    }
}

# ================== CUSTOM CSS: LIGHT PURPLE THEME ==================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ce93d8 0%, #ab47bc 100%);
        border-right: 2px solid #6a1b9a;
    }
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stCaption {
        color: #1a1a2e !important;
    }
    [data-testid="stSidebar"] .stSelectbox label {
        color: #1a1a2e !important;
        font-weight: bold !important;
        font-size: 1rem !important;
    }
    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] span {
        color: #1a1a2e !important;
        font-weight: bold !important;
    }
    div[data-baseweb="select"] ul {
        background-color: #e1bee7 !important;
    }
    div[data-baseweb="select"] ul li {
        color: #1a1a2e !important;
        font-weight: bold !important;
        background-color: #e1bee7 !important;
    }
    div[data-baseweb="select"] ul li:hover {
        background-color: #ba68c8 !important;
    }
    h1, h2, h3 {
        color: #4a148c !important;
    }
    p, li, .stMarkdown {
        color: #1a1a2e !important;
    }
    .stButton>button {
        background-color: #8e24aa !important;
        color: white !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ab47bc !important;
        transform: scale(1.02);
    }
    .security-badge {
        background: #f3e5f5;
        border: 1px solid #6a1b9a;
        border-radius: 30px;
        padding: 8px 15px;
        margin: 10px 0;
        text-align: center;
        color: #4a148c;
        font-weight: bold;
    }
    .feature-card {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# ================== SIDEBAR ==================
with st.sidebar:
    st.image("https://raw.githubusercontent.com/Deslandes1/Color-Software-Game/main/Gesner%20Deslandes.png", width=80)
    st.markdown("## **GlobalInternet.py**")
    st.markdown("**ICPC Practice Arena**")
    st.markdown("---")
    
    # Language selection
    language = st.selectbox("🌐 Language / Idioma / Langue", ["English", "Français", "Español"])
    texts = TEXTS[language]
    
    # Global Security Shield (API key hidden)
    st.markdown("---")
    st.markdown("### 🛡️ Global Security Shield active")
    st.markdown(f'<div class="security-badge">{texts["security_badge"]}</div>', unsafe_allow_html=True)
    st.caption(texts["security_caption"])
    
    st.markdown("---")
    st.markdown("Built by **Gesner Deslandes**, Engineer-in-Chief")
    st.markdown("📞 (509) 4738 5663")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("---")
    
    # Pricing
    st.markdown(f"### 💰 {texts['price_title']}")
    for item in texts["price_list"]:
        st.markdown(f"- {item}")
    st.markdown("---")
    
    st.markdown(f"### {texts['sidebar_howto']}")
    for i, step in enumerate(texts["howto_list"], 1):
        st.markdown(f"{i}. {step}")

# ================== MAIN TITLE ==================
st.title(texts["title"])
st.markdown(f"### {texts['subtitle']}")
st.markdown("---")

# ================== GROQ CLIENT ==================
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ Missing Groq API key. Add `GROQ_API_KEY` to your Streamlit secrets.")
    st.stop()
groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ================== HELPER: AI FEEDBACK ==================
def get_ai_feedback(user_input, language):
    system_prompt = f"""You are an expert ICPC coach. The user has written the following code or algorithm idea for the Longest Increasing Subsequence problem. Provide constructive feedback:
- Point out inefficiencies (e.g., O(n²) when O(n log n) is expected).
- Suggest improvements.
- Explain key concepts if missing.
Keep your answer concise and helpful. Respond in {language}."""
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3,
            max_tokens=800
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return texts["ai_error"].format(str(e))

# ================== TABS ==================
tab1, tab2, tab3 = st.tabs([texts["video_tab"], texts["practice_tab"], texts["ai_tab"]])

# ---------- Tab 1: Video Introduction ----------
with tab1:
    st.markdown(f"### {texts['video_title']}")
    st.markdown(texts['video_desc'])
    # Pre-filled Dropbox link (use dl=1); user can change it
    default_video = "https://www.dropbox.com/scl/fi/example.mp4?dl=1"
    video_url = st.text_input(texts["video_placeholder"], value=default_video)
    if video_url:
        st.video(video_url)
    else:
        st.info("No video link provided. You can record a walkthrough and paste the link here.")

# ---------- Tab 2: Practice Problem ----------
with tab2:
    st.markdown(f"### {texts['problem_title']}")
    st.markdown(texts['problem_statement'])
    user_array = st.text_input(texts["test_input"], value="10,9,2,5,3,7,101,18")
    if st.button(texts["run_button"]):
        try:
            arr = [int(x.strip()) for x in user_array.split(",") if x.strip()]
            if not arr:
                st.error("Invalid input.")
            else:
                # O(n log n) LIS calculation
                import bisect
                tails = []
                for x in arr:
                    i = bisect.bisect_left(tails, x)
                    if i == len(tails):
                        tails.append(x)
                    else:
                        tails[i] = x
                lis_len = len(tails)
                st.success(texts["result_correct"].format(lis_len))
        except Exception as e:
            st.error(f"Error: {e}")

# ---------- Tab 3: AI Coach ----------
with tab3:
    st.markdown(f"### 🤖 {texts['ai_tab']}")
    user_code = st.text_area(texts["hint_placeholder"], height=250,
                             placeholder="Example: def lis(arr):\n    n = len(arr)\n    dp = [1]*n\n    for i in range(n):\n        for j in range(i):\n            if arr[j] < arr[i]:\n                dp[i] = max(dp[i], dp[j]+1)\n    return max(dp)")
    if st.button(texts["hint_button"]):
        if not user_code.strip():
            st.warning("Please describe your approach or paste your code.")
        else:
            with st.spinner(texts["ai_thinking"]):
                feedback = get_ai_feedback(user_code, language)
            st.markdown("### 💡 AI Feedback")
            st.markdown(feedback)

# ================== FOOTER ==================
st.markdown("---")
st.markdown(texts["footer"])
