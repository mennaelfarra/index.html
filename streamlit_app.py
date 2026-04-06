import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Interactive Map Project",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(59,130,246,0.22), transparent 28%),
        radial-gradient(circle at top right, rgba(168,85,247,0.18), transparent 22%),
        linear-gradient(135deg, #0b1020 0%, #111827 35%, #1e293b 70%, #0f172a 100%);
}

.block-container {
    max-width: 1240px;
    padding-top: 1.8rem;
    padding-bottom: 2rem;
}

.hero {
    position: relative;
    overflow: hidden;
    border-radius: 28px;
    padding: 44px 34px;
    margin-bottom: 20px;
    background: linear-gradient(135deg, rgba(37,99,235,0.22), rgba(139,92,246,0.18));
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 18px 50px rgba(0,0,0,0.28);
}

.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.04), transparent);
    transform: translateX(-100%);
    animation: shine 5s infinite;
}

@keyframes shine {
    100% { transform: translateX(100%); }
}

.hero-title {
    text-align: center;
    color: #ffffff;
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 10px;
    letter-spacing: 0.3px;
}

.hero-subtitle {
    text-align: center;
    color: #dbeafe;
    font-size: 1.08rem;
    line-height: 1.8;
    max-width: 900px;
    margin: 0 auto 18px auto;
}

.badges {
    text-align: center;
    margin-top: 8px;
}

.badge {
    display: inline-block;
    margin: 6px 4px;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(255,255,255,0.08);
    color: #e0f2fe;
    border: 1px solid rgba(255,255,255,0.10);
    font-size: 0.90rem;
    font-weight: 600;
    box-shadow: 0 0 18px rgba(59,130,246,0.12);
}

.card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 22px;
    padding: 22px;
    min-height: 185px;
    box-shadow: 0 12px 32px rgba(0,0,0,0.16);
    backdrop-filter: blur(10px);
}

.card h3 {
    color: #ffffff;
    margin: 0 0 10px 0;
    font-size: 1.15rem;
}

.card p {
    color: #dbeafe;
    line-height: 1.8;
    font-size: 0.97rem;
    margin: 0;
}

.section-title {
    text-align: center;
    color: #ffffff;
    font-size: 2rem;
    font-weight: 800;
    margin-top: 26px;
    margin-bottom: 8px;
}

.section-subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 18px;
    font-size: 1rem;
}

.map-shell {
    background: rgba(255,255,255,0.96);
    border-radius: 26px;
    padding: 14px;
    box-shadow: 0 22px 50px rgba(0,0,0,0.24);
    margin-bottom: 14px;
}

.chat-wrap {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 24px;
    padding: 18px;
    box-shadow: 0 12px 32px rgba(0,0,0,0.18);
    margin-top: 18px;
}

.chat-title {
    color: white;
    font-size: 1.35rem;
    font-weight: 800;
    margin-bottom: 4px;
}

.chat-subtitle {
    color: #dbeafe;
    margin-bottom: 10px;
    font-size: 0.96rem;
}

.footer-note {
    text-align: center;
    color: #cbd5e1;
    margin-top: 18px;
    font-size: 0.95rem;
}

div.stButton > button {
    width: 100%;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.10);
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    font-weight: 700;
    padding: 0.75rem 1rem;
    box-shadow: 0 0 22px rgba(99,102,241,0.35);
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 0 28px rgba(99,102,241,0.55);
    border-color: rgba(255,255,255,0.22);
}

div[data-testid="stTextArea"] textarea {
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.18) !important;
    background: rgba(255,255,255,0.95) !important;
}

.chat-bubble-user {
    background: linear-gradient(135deg, #2563eb, #4f46e5);
    color: white;
    padding: 12px 14px;
    border-radius: 16px 16px 4px 16px;
    margin: 8px 0 8px auto;
    width: fit-content;
    max-width: 90%;
    box-shadow: 0 0 16px rgba(59,130,246,0.24);
}

.chat-bubble-ai {
    background: rgba(255,255,255,0.96);
    color: #111827;
    padding: 12px 14px;
    border-radius: 16px 16px 16px 4px;
    margin: 8px auto 8px 0;
    width: fit-content;
    max-width: 90%;
    box-shadow: 0 0 16px rgba(255,255,255,0.09);
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
<div class="hero">
    <div class="hero-title">🌍 Interactive Map Project</div>
    <div class="hero-subtitle">
        A premium GIS web application for exploring an interactive map experience with a polished interface,
        elegant gradients, and an integrated AI assistant for quick user questions.
    </div>
    <div class="badges">
        <span class="badge">GIS</span>
        <span class="badge">Python</span>
        <span class="badge">Streamlit</span>
        <span class="badge">Leafmap</span>
        <span class="badge">AI Assistant</span>
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <h3>📌 Project Overview</h3>
        <p>
            This application presents geographic data through an interactive map in a modern and accessible layout,
            suitable for competitions, portfolios, and academic presentations.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h3>🛠 Technologies Used</h3>
        <p>
            Built with Python, Streamlit, HTML map export, and GIS workflows to provide
            a polished interactive mapping experience online.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h3>🎯 Purpose</h3>
        <p>
            The goal is to deliver a professional and intelligent map experience that allows users
            to view the map visually and interact with a guided support chat.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">Explore the Interactive Map</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Zoom, pan, and use the map controls to interact with the visualization.</div>', unsafe_allow_html=True)

# ---------- Map ----------
map_url = "https://raw.githack.com/mennaelfarra/index.html/main/map.html"

st.markdown('<div class="map-shell">', unsafe_allow_html=True)
components.iframe(map_url, height=700, scrolling=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- AI Chat ----------
st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)
st.markdown('<div class="chat-title">💬 AI Chat Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="chat-subtitle">Ask anything related to the project, the map, locations, layers, or how to use the interface.</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-bubble-user">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble-ai">{msg["content"]}</div>', unsafe_allow_html=True)

user_prompt = st.text_area(
    "Write your question",
    placeholder="Example: What does this map show?",
    label_visibility="collapsed",
    height=110
)

col_btn1, col_btn2 = st.columns([1, 4])

with col_btn1:
    send_clicked = st.button("Send")

with col_btn2:
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if send_clicked and user_prompt.strip():
    st.session_state.messages.append({"role": "user", "content": user_prompt.strip()})

    answer = """
💬 مرحباً بك 🌟

هذه الدردشة موجودة لدعم فكرة المشروع فقط،
وهي حالياً غير مؤهلة بعد للرد على أسئلتك واستفساراتك 

شكراً لمرورك
Menna Elfarra ✨
"""

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer-note">Created by Menna • Professional Interactive GIS Web App</div>', unsafe_allow_html=True)