# Auto Movie Scraper & Recommendation System

A fully automated pipeline that scrapes the latest movies from TMDB, processes them with NLP, and generates movie recommendations using a content-based filtering model. A web interface is provided via Streamlit, and the entire pipeline is automated using GitHub Actions. The web app is deployed using Render.

## Features

- Automated monthly scraping of movie data using TMDB API
- NLP-based content filtering using genres, keywords, cast, and overview
- Preprocessed data stored in .pkl files for fast web access
- GitHub Actions workflow for automated data updates
- Streamlit-based movie recommendation web app hosted on Render

## Project Structure

.
├── main.py                  # Executes scraping + recommendation generation  
├── api.py                   # TMDB API logic and data preprocessing  
├── requirements.txt         # Dependencies for scraping pipeline  
├── .github/workflows/  
│   └── scrape.yml           # GitHub Actions automation  
└── webapp/                  # Root for Streamlit deployment on Render  
    ├── app.py               # Streamlit web application  
    ├── requirements.txt     # Dependencies for web app  
    ├── movies.pkl           # Serialized movie data  
    └── similarity.pkl       # Cosine similarity matrix  

## How It Works

1. `main.py` scrapes and processes TMDB data, then saves `movies.pkl` and `similarity.pkl`.
2. GitHub Actions triggers monthly or manually, runs the pipeline, and pushes updates.
3. Streamlit app loads .pkl files and displays top movie recommendations.

## Requirements

Install scraping dependencies:
pip install -r requirements.txt

Run scraping:
python main.py

Install and run the web app:
cd webapp/
pip install -r requirements.txt
streamlit run app.py

## Secrets Configuration

Set the following secrets in your GitHub repo:

- `API_KEY`: Your TMDB API key  
- `GH_PAT`: GitHub personal access token with repo permissions  

## GitHub Actions

The workflow runs monthly using:
cron: '39 04 1 * *'

You can also run it manually via the Actions tab.

## Deployment (Render)

Deploy the `webapp/` folder on Render:
- Build command: pip install -r requirements.txt
- Start command: streamlit run app.py
- Make sure `.pkl` files are in the same folder

## Acknowledgements

- TMDB API
- NLTK
- Streamlit
- GitHub Actions
