# 🚨 SIR IS COMING! — Streamlit Deployment Project

A browser-based 2D classroom stealth and survival game, packaged with a Streamlit launcher so it can be deployed on **Streamlit Community Cloud**.

## Project structure

```text
Sir_Is_Coming_Streamlit/
├── app.py                       # Streamlit entrypoint (deploy this file)
├── requirements.txt             # Python dependency
├── README.md                    # This guide
├── .gitignore
├── run_local.bat                # Windows local launcher
├── run_local.sh                 # macOS/Linux local launcher
├── .streamlit/
│   └── config.toml              # Streamlit theme and toolbar settings
├── game/
│   └── index.html               # Complete HTML/CSS/JavaScript game
└── assets/
    └── gameplay_preview.png     # Preview image for README/project page
```

The game is self-contained in `game/index.html` (CSS and JavaScript are embedded in that file). It does not load external images, fonts, or JavaScript libraries.

## Run locally in VS Code

1. Extract this project ZIP.
2. Open the **Sir_Is_Coming_Streamlit** folder in VS Code.
3. Open the VS Code terminal in this folder.
4. Run:

   ```bash
   python -m pip install -r requirements.txt
   python -m streamlit run app.py
   ```

5. Open the local URL printed in the terminal (usually `http://localhost:8501`).
6. Click inside the game once, then use the keyboard. Touch controls appear on small screens.

On Windows, you can also double-click `run_local.bat`. On macOS/Linux, run `./run_local.sh` from a terminal.

## Upload to GitHub

**Upload the contents of this folder to the root of a GitHub repository**. Do not upload only the ZIP file, and do not leave the files nested inside an extra folder level.

The repository root should show:

- `app.py`
- `requirements.txt`
- `game/index.html`
- `.streamlit/config.toml`

You can upload through GitHub's web interface (Add file → Upload files), or use Git:

```bash
git init
git add .
git commit -m "Prepare SIR IS COMING for Streamlit deployment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the GitHub URL with your own repository URL.

## Deploy on Streamlit Community Cloud

1. Push the project to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/) and sign in.
3. Select **Create app** → **Yup, I have an app**.
4. Choose your GitHub repository.
5. Select branch: `main` (or the branch you pushed).
6. Set **Main file path** to exactly: `app.py`
7. Click **Deploy**.

Streamlit installs the dependency from `requirements.txt` and runs `app.py`. The app embeds the local `game/index.html` file using `st.iframe`.

## Controls

| Key | Action |
|---|---|
| WASD / Arrow keys | Move |
| Shift | Run |
| E | Interact |
| H | Hide / leave hiding |
| Q | Character ability |
| 1 | Use inventory item |
| Esc | Pause |

On mobile, use the on-screen directional and action buttons.

## Notes

- The game runs in the browser; Streamlit is the deployment shell/launcher.
- Game progress and best scores are saved in the current browser's local storage. They are not a shared online leaderboard and do not automatically sync between devices.
- Because the HTML game is trusted project code, it is embedded directly in an iframe. Do not replace it with untrusted user-supplied HTML.
- Streamlit Community Cloud deployment requires the GitHub repository to contain the full project structure above.
