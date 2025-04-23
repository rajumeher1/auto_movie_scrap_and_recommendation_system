from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorize_tags(data):
    cv = CountVectorizer(max_features=1000)
    vectors = cv.fit_transform(data)
    return vectors

def compute_similarity(vectors):
    cs = cosine_similarity(vectors)
    top_10_similarity =[]
    for i in range(len(cs)):
        similarity = list(enumerate(cs[i]))
        similarity = sorted(similarity, key=lambda x: x[1])[1:11]
        top_10_similarity.append([i[0] for i in similarity])
    
    return top_10_similarity