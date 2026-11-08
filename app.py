from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parent


def find_game_file(root: Path) -> Path | None:
    """Find the game whether index.html is in /game or at the repository root.

    The user's current GitHub upload has index.html beside app.py (root-level),
    while an earlier package expected game/index.html. Both layouts are valid.
    """
    candidates = [
        root / "game" / "index.html",   # recommended layout
        root / "index.html",             # flattened GitHub upload layout
        root / "Game" / "index.html",   # case variant
        root / "game" / "Index.html",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate

    # Handle one extra enclosing directory or a folder renamed during upload.
    ignored = {
        ".git", ".venv", "venv", "__pycache__", ".streamlit",
        "node_modules", "site-packages",
    }
    matches: list[Path] = []
    try:
        for path in root.rglob("*.html"):
            try:
                parts = [p.lower() for p in path.relative_to(root).parts]
            except ValueError:
                continue
            if any(part in ignored for part in parts):
                continue
            if path.is_file() and path.name.lower() == "index.html":
                matches.append(path)
    except OSError:
        pass

    if not matches:
        return None

    # Prefer a file inside a folder named "game", then the shallowest path.
    def rank(path: Path):
        parts = [p.lower() for p in path.relative_to(root).parts]
        in_game_folder = 0 if len(parts) >= 2 and parts[-2] == "game" else 1
        return (in_game_folder, len(parts), str(path).lower())

    matches.sort(key=rank)
    return matches[0]


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

GAME_FILE = find_game_file(ROOT)

if GAME_FILE is None:
    st.error("Game file not found. Please upload index.html to the repository root or to game/index.html.")
    st.markdown("Your GitHub repository should contain **one** of these layouts:")
    st.code(
        "Option A (recommended):\n"
        "repository-root/\n"
        "├── app.py\n"
        "├── requirements.txt\n"
        "└── game/\n"
        "    └── index.html\n\n"
        "Option B (also supported):\n"
        "repository-root/\n"
        "├── app.py\n"
        "├── requirements.txt\n"
        "└── index.html",
        language="text",
    )
    st.caption("Files currently visible beside app.py:")
    try:
        entries = sorted(p.name + ("/" if p.is_dir() else "") for p in ROOT.iterdir() if p.name != ".git")
        st.code("\n".join(entries) if entries else "<repository is empty>")
    except OSError as exc:
        st.code(str(exc))
    st.stop()

# IMPORTANT: Pass a pathlib.Path, not str(GAME_FILE), to st.iframe.
# Current Streamlit versions read local HTML files from Path objects.
st.iframe(
    GAME_FILE,
    width="stretch",
    height=900,
    tab_index=0,
    alt="SIR IS COMING! classroom survival game",
)

st.caption(
    f"Loaded game file: {GAME_FILE.relative_to(ROOT)} · "
    "Tip: click inside the game before using the keyboard. On mobile, use the on-screen controls."
)
