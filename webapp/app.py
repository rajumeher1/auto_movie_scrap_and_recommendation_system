from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import random

app = FastAPI()

# Mount the Statice directory
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


# Load the Movies
with open('movie_list.pkl', 'rb') as f:
    movie_list = pickle.load(f)

with open('similar_movies.pkl', 'rb') as f:
    top_similar_movies = pickle.load(f)

# Reccomentation Function
def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    similar_movie_list = top_similar_movies[movie_index]
    similar_5_movies = random.sample(similar_movie_list, 5)

    recommended_list = []
    poster_path_list = []
    for i in similar_5_movies:
        recommended_list.append(movie_list.iloc[i]['title'])
        poster_path_list.append(movie_list.iloc[i]['poster_path'])

    return recommended_list, poster_path_list

# Handle get request to display form
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    movie_list_titles = movie_list['title'].tolist()
    return templates.TemplateResponse('index.html', {
        'request': request,
        'movie_list_titles': movie_list_titles,
        'reccomendations': None
    })

@app.post('/', response_class=HTMLResponse)
async def recommend_movie(request: Request, movie: str = Form(...)):
    movie_list_titles = movie_list['title'].tolist()

    if movie not in movie_list_titles:
        return templates.TemplateResponse('index.html', {
            'request': request,
            'error': 'Movie not found in the list. Please type a valid movie name.',
            'movie_list_titles': movie_list_titles,
            'recommendations': None
        })
    
    recommended_movie_list, poster_path_list = recommend(movie)
    recommendations = list(zip(recommended_movie_list, poster_path_list))
    return templates.TemplateResponse('index.html', {
        'request': request,
        'movie': movie,
        'recommendations': recommendations,
        'movie_list_titles': movie_list_titles 
    })