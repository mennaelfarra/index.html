import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Interactive Map Project",
    page_icon="🌍",
    layout="wide",
)

st.title("🌍 Interactive Map Project")
st.markdown(
    "This project displays an interactive map built with Python and GIS tools."
)

map_file = Path("map.html")

if map_file.exists():
    html_content = map_file.read_text(encoding="utf-8")
    components.html(html_content, height=700, scrolling=True)
else:
    st.error("map.html file was not found in the repository.")