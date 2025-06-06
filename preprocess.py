import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_dataframe(df):
    df = df.dropna(how='any')
    df = df[df.apply(lambda row: all(val != '' and val != [] for val in row), axis=1)]
    df = df.drop_duplicates(subset=df.columns[:3])
    return df.reset_index(drop=True)

def clean_text_column(df):
    df['new_title'] = df['title'].apply(lambda x: x.split())
    df["overview"] = df["overview"].apply(lambda x: x.split())

    col_list = ['genres', 'keywords', 'cast', 'director']
    for col in col_list:
        df[col] = df[col].apply(lambda x: [i.replace(' ', '') for i in x])
    return df

def preprocess_tags(word_list):
    cleaned = []

    for word in word_list:
        word = word.lower()
        word = word.translate(str.maketrans('','', string.punctuation))
        if word and word not in stop_words:
            stemmed = ps.stem(word)
            cleaned.append(stemmed)
    return ' '.join(cleaned)

def create_tags_column(df):
    df['tags'] = df['new_title'] + df['genres'] + df['keywords'] + df['cast'] + df['director'] + df['overview']
    df['tags'] = df['tags'].apply(preprocess_tags)
    return df