# SIR IS COMING! — Streamlit Deployment Project

This repository runs the browser game inside a Streamlit page using `st.iframe`.

## Important: correct GitHub folder structure

`app.py` and `requirements.txt` must be at the **repository root**. The game file must be at `game/index.html` relative to `app.py`.

```text
repository-root/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml
├── assets/
│   └── gameplay_preview.png
└── game/
    └── index.html
```

Do not upload the ZIP file itself as the only repository file. Extract it first, then upload the contents of this project folder. Do not accidentally create `Sir_Is_Coming_Streamlit_Fixed/Sir_Is_Coming_Streamlit_Fixed/app.py` or nest `game/` under another folder.

The app now also searches for a nested `game/index.html` path to recover from common extra-folder upload mistakes. The recommended structure above is still best.

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload **the contents of this folder** to the repository root.
3. Open [Streamlit Community Cloud](https://share.streamlit.io/).
4. Choose **Create app** and select the GitHub repository.
5. Set branch to `main` (or your selected branch).
6. Set **Main file path** to `app.py`.
7. Click **Deploy**.

## Run locally

Python 3.10+ is recommended.

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Troubleshooting the missing game file error

If the app still says the game file is missing, open the GitHub repository page and confirm that `game/index.html` is visible in the root-level `game` folder. The app's error screen also displays the repository's top-level entries to help diagnose an incorrect upload path.
