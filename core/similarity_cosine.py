from sklearn.metrics.pairwise import cosine_similarity


def calc_cosine_similarity(vector1, vector2):
    return cosine_similarity([vector1, vector2])
