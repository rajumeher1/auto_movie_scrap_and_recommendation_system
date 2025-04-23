import streamlit as st
import pickle
import random


with open("movie_list.pkl", 'rb') as f:
    movie_list = pickle.load(f)

with open("similar_movies.pkl", 'rb') as f:
    top_similar_movie = pickle.load(f)

def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    similar_movie_list = top_similar_movie[movie_index]
    similar_5_movies = random.sample(similar_movie_list, 5)

    recommended_list = []
    poster_path_list = []
    for i in similar_5_movies:
        recommended_list.append(movie_list.iloc[i]['title'])
        poster_path_list.append(movie_list.iloc[i]['poster_path'])
    
    return recommended_list, poster_path_list

st.set_page_config(
    page_title="My Movie Recommender",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/your_repo/help',
        'Report a bug': 'https://github.com/your_repo/issues',
        'About': "This app recommends movies based on what you like! 🍿"
    }
)

st.subheader("TMDB Movie Recommendation System")

movie = st.selectbox(
    " ",
    (movie_list['title']),
    index=None,
    placeholder='Type/Find a Movie Name you have already watched'
)

if st.button('Find Similar Movies'):
    if movie == None:
        st.write("Please enter a movie name above so I can recommend similar ones you might enjoy!")
    else:
        st.markdown(f":orange[****Check out these movies that are similar to '{movie}'****]")
        recommended_list, poster_path_list = recommend(movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(f"https://image.tmdb.org/t/p/w500{poster_path_list[0]}", caption=f"{recommended_list[0]}")
        with col2:
            st.image(f"https://image.tmdb.org/t/p/w500{poster_path_list[1]}", caption=f"{recommended_list[1]}")
        with col3:
            st.image(f"https://image.tmdb.org/t/p/w500{poster_path_list[2]}", caption=f"{recommended_list[2]}")
        with col4:
            st.image(f"https://image.tmdb.org/t/p/w500{poster_path_list[3]}", caption=f"{recommended_list[3]}")
        with col5:
            st.image(f"https://image.tmdb.org/t/p/w500/{poster_path_list[4]}", caption=f"{recommended_list[4]}")




