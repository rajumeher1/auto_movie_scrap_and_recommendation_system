import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.themoviedb.org/3'
TOTAL_PAGES = 50

if not API_KEY:
        raise ValueError("API_KEY not set in enviromental variables")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrap_movies():
    logging.info("Movie Scraping Started...")
    movie_list = []

    try:            
        for page in range(1, TOTAL_PAGES + 1):

            if page % 50 == 0:
                logging.info(f"fetched {page} pages so far, continuing with the rest...")

            params = {
                'api_key': API_KEY,
                'language': 'en-US',
                'page': page
            }
            response = requests.get(url=f"{BASE_URL}/discover/movie", params=params)
            result = response.json()

            for movie in result.get('results', []):
                movie_item = {
                    'id': movie['id'],
                    'title': movie['title'],
                    'poster_path': movie['poster_path'],
                    "overview": movie["overview"]
                }
                details_url = f"{BASE_URL}/movie/{movie['id']}"
                details_params = {
                    'api_key': API_KEY,
                    'append_to_response': 'keywords,credits'
                }
                dt_response = requests.get(url=details_url, params=details_params)
                dt_data = dt_response.json()

                if 'genres' not in dt_data or 'keywords' not in dt_data or 'credits' not in dt_data:
                    continue

                movie_item['genres'] = [i['name'] for i in dt_data['genres']]
                movie_item['keywords'] = [i['name'] for i in dt_data['keywords']['keywords']]
                movie_item['cast'] = [i['name'] for i in dt_data['credits']['cast']][:3]
                movie_item['director'] = [i['name'] for i in dt_data['credits']['crew'] if i['job'] == 'Director']

                movie_list.append(movie_item)
        logging.info("Movie Scraping completed successfully.")
    
    except Exception as e:
        logging.error(f"An error occured: {e}")

    return movie_list
