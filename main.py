import pandas as pd
from api import scrap_movies
from preprocess import clean_dataframe, clean_text_column, create_tags_column
from vectorizer import vectorize_tags, compute_similarity
from save_utils import save_movies_list, save_similarity


def run_all():
    movie_list = scrap_movies()
    df = pd.DataFrame(movie_list)

    df = clean_dataframe(df)
    df = clean_text_column(df)
    df = create_tags_column(df)

    vectors = vectorize_tags(df['tags'])
    similarity = compute_similarity(vectors)

    save_movies_list(df)
    save_similarity(similarity)


if __name__=='__main__':
    run_all()