from preprocess import preprocess_text
import pandas as pd
import os
from feature_extraction import tfidf_features
from similarity_cosine import calc_cosine_similarity


df = pd.read_csv("stopwords.csv")
amharic_stopwords = df["stopword"].tolist()

file_names = [file for file in os.listdir("./test_docs") if file.endswith(".txt")]
docs = [open(f"./test_docs/{file}", encoding="utf-8").read() for file in file_names]

preprocessed_docs = [preprocess_text(doc, amharic_stopwords) for doc in docs]

doc_vec = tfidf_features(preprocessed_docs)
doc_filename_pairs = list(zip(file_names, doc_vec))


def check_plagiarism():

    plagiarism_results = set()

    global doc_filename_pairs

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
                similarity_score,
            )
            plagiarism_results.add(plagiarism_result)

    return plagiarism_results


results = check_pliagrism()

for x in results:
    print(x)
