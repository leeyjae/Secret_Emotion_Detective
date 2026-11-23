# Secret Emotion Detective

A two-player English activity built with Streamlit. Student A and Student B
receive different blanks so they can practice asking and answering questions.

## Run locally

Install the project dependencies and start the app:

```bash
uv sync
uv run streamlit run streamlit_app.py
```

## Share the app online

The app can be hosted for free on [Streamlit Community Cloud](https://streamlit.io/cloud).

1. Push this project to a GitHub repository. Make it public if you want anyone
   to be able to view the source code.
2. Sign in to Streamlit Community Cloud with GitHub and select **Create app**.
3. Choose this repository and the branch you want to deploy.
4. Set **Main file path** to `streamlit_app.py`, then select **Deploy**.
5. Share the URL Streamlit gives you. Anyone who can access that URL can use
   the app; this app does not require sign-in.

The repository already includes its Python dependencies. If you add API keys
or other credentials later, enter them in the app's Community Cloud secrets
settings instead of committing them to GitHub.
