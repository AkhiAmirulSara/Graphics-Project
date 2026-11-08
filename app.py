from pathlib import Path

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parent
GAME_FILE = ROOT_DIR / "game" / "index.html"

st.set_page_config(
    page_title="SIR IS COMING! | Classroom Survival",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep the Streamlit shell visually minimal so the game is the main focus.
st.markdown(
    """
    <style>
      .stApp, [data-testid="stAppViewContainer"] {
        background: #07182b;
      }
      [data-testid="stMainBlockContainer"] {
        max-width: 100%;
        padding: 0.35rem 0.65rem 0.15rem 0.65rem;
      }
      [data-testid="stHeader"] {
        background: transparent;
      }
      [data-testid="stToolbar"], footer, #MainMenu {
        visibility: hidden;
        height: 0;
      }
      iframe {
        border: 0 !important;
        border-radius: 12px;
      }
      @media (max-width: 700px) {
        [data-testid="stMainBlockContainer"] {
          padding: 0.1rem 0.1rem 0 0.1rem;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

if not GAME_FILE.is_file():
    st.error("Game file is missing. Expected: game/index.html")
    st.stop()

st.iframe(
    GAME_FILE,
    width="stretch",
    height=900,
    alt="SIR IS COMING! interactive 2D classroom stealth and survival game",
)

st.caption(
    "Tip: click inside the game before using the keyboard. "
    "On phones and tablets, use the on-screen controls."
)
