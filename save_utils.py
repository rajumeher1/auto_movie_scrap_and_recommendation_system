import pickle

def save_movies_list(df):
    df = df[['id', 'title', 'poster_path']]
    with open("webapp/movies.pkl", 'wb') as f:
        pickle.dump(df, f)

def save_similarity(data):
    with open('webapp/similarity.pkl', 'wb') as f:
        pickle.dump(data, f)