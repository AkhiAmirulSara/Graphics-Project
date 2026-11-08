from pathlib import Path
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent


def find_game_file(root: Path) -> Path | None:
    """Find game/index.html even if the project folder was uploaded one level too deep."""
    candidates = [
        root / "game" / "index.html",
        root / "Sir_Is_Coming_Streamlit" / "game" / "index.html",
        root / "Sir_Is_Coming_Streamlit_Fixed" / "game" / "index.html",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate

    # GitHub uploads sometimes create an extra enclosing project directory.
    # Search for a case-insensitive game/index.html path while skipping bulky folders.
    ignored = {".git", ".venv", "venv", "__pycache__", ".streamlit"}
    for path in root.rglob("index.html"):
        try:
            relative_parts = [part.lower() for part in path.relative_to(root).parts]
        except ValueError:
            continue
        if any(part in ignored for part in relative_parts):
            continue
        if len(relative_parts) >= 2 and relative_parts[-2:] == ["game", "index.html"] and path.is_file():
            return path
    return None


st.set_page_config(
    page_title="SIR IS COMING! | Classroom Survival",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .stApp, [data-testid="stAppViewContainer"] { background: #07182b; }
      [data-testid="stMainBlockContainer"] { max-width: 100%; padding: .3rem .55rem .1rem; }
      [data-testid="stHeader"] { background: transparent; }
      [data-testid="stToolbar"], footer, #MainMenu { visibility: hidden; height: 0; }
      iframe { border: 0 !important; border-radius: 12px; }
      @media (max-width: 700px) {
        [data-testid="stMainBlockContainer"] { padding: .1rem; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

GAME_FILE = find_game_file(ROOT_DIR)

if GAME_FILE is None:
    st.error("Game file could not be found in this GitHub repository.")
    st.markdown(
        "The expected path is **`game/index.html`**, relative to `app.py`. "
        "Upload the complete `game` folder beside `app.py`, or upload the contents "
        "of the ZIP at the repository root."
    )
    st.code(
        "repository-root/\n"
        "├── app.py\n"
        "├── requirements.txt\n"
        "└── game/\n"
        "    └── index.html",
        language="text",
    )
    st.caption("For troubleshooting, files visible at the repository root:")
    try:
        entries = sorted(p.name + ("/" if p.is_dir() else "") for p in ROOT_DIR.iterdir() if p.name != ".git")
        st.code("\n".join(entries) if entries else "<repository is empty>")
    except OSError as exc:
        st.code(str(exc))
    st.stop()

# st.iframe supports a local HTML file and keeps the game's JavaScript inside an iframe.
st.iframe(
    GAME_FILE,
    width="stretch",
    height=900,
    tab_index=0,
)

st.caption(
    "Tip: click inside the game before using the keyboard. "
    "On phones and tablets, use the on-screen controls."
)
