import streamlit as st
from google import genai

# Mobile Layout Configuration
st.set_page_config(
    page_title="Mobile Content Engine",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Mobile CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 3em;
        font-size: 18px !important;
        border-radius: 10px;
    }
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📱 Content OS")
st.caption("On-the-go Content & Product Generator")

# API Key handling
api_key = st.secrets.get("GEMINI_API_KEY") if "GEMINI_API_KEY" in st.secrets else None

if not api_key:
    with st.expander("🔑 API Key Setup"):
        api_key = st.text_input("Enter Gemini API Key", type="password")

if not api_key:
    st.info("Enter your Gemini API key above to unlock mobile controls.")
    st.stop()

client = genai.Client(api_key=api_key)

# Mobile Form Controls
st.subheader("1. Core Concept")
mode = st.selectbox("Action Mode", [
    "⚡ Full Content Suite (YouTube + Email + Lead Magnet)",
    "🎬 YouTube Script & Teleprompter",
    "📲 5 Short-Form Hooks (TikTok/Reels)",
    "💡 Lead Magnet / Playbook Outline"
])

topic = st.text_area(
    "Idea or Voice Dictation Prompt",
    placeholder="Tap your phone microphone icon to dictate your raw idea here...",
    height=120
)

target_niche = st.text_input("Niche / Audience", value="Relationship Psychology & Digital Products")

if st.button("🚀 Generate Assets"):
    if not topic.strip():
        st.warning("Please enter or dictate a topic first.")
        st.stop()
        
    with st.spinner("Processing idea on cloud server..."):
        prompt = f"""
        You are a top-tier digital content strategist for the niche: '{target_niche}'.
        Target Mode: {mode}
        Core Topic/Idea: '{topic}'
        
        Generate actionable, highly structured content optimized for mobile reading.
        Use clean Markdown headings, bullet points, and copyable text blocks.
        """
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        st.markdown("---")
        st.subheader("2. Generated Output")
        st.markdown(response.text)
        
        st.download_button(
            label="💾 Save Output (.md)",
            data=response.text,
            file_name="mobile_content_draft.md",
            mime="text/markdown"
      )
      
