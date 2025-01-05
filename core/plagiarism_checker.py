import os
import pandas as pd
from core.preprocess import preprocess_text
from core.feature_extraction import tfidf_features
from core.similarity_cosine import calc_cosine_similarity


df = pd.read_csv("stopwords.csv")
amharic_stopwords = df["stopword"].tolist()


def check_plagiarism(file_paths):

    print(file_paths)
    docs = [open(file, encoding="utf-8").read() for file in file_paths]
    preprocessed_docs = [preprocess_text(doc, amharic_stopwords) for doc in docs]
    print(preprocessed_docs)
    # Generate TF-IDF vectors
    doc_vec = tfidf_features(preprocessed_docs)
    doc_filename_pairs = list(
        zip([os.path.basename(file) for file in file_paths], doc_vec)
    )

    plagiarism_results = set()

    for a_file, a_vec in doc_filename_pairs:
        remaining_pairs = doc_filename_pairs.copy()
        current_index = remaining_pairs.index((a_file, a_vec))
        del remaining_pairs[current_index]

        for b_file, b_vec in remaining_pairs:
            similarity_score = float(calc_cosine_similarity(a_vec, b_vec)[0][1])

            sorted_filenames = sorted((a_file, b_file))
            plagiarism_result = (
                sorted_filenames[0],
                sorted_filenames[1],
                round(similarity_score * 100, 2),
            )
            plagiarism_results.add(plagiarism_result)
    return plagiarism_results
