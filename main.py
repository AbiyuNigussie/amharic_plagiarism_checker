from preprocess import preprocess_text
import pandas as pd
import os


def check_pliagrism():
    df = pd.read_csv("stopwords.csv")
    amharic_stopwords = df["stopword"].tolist()

    student_file = [file for file in os.listdir("./test_docs") if file.endswith(".txt")]
    student_docs = [
        open(f"./test_docs/{file}", encoding="utf-8").read() for file in student_file
    ]

    preprocessed_docs = [
        preprocess_text(doc, amharic_stopwords) for doc in student_docs
    ]

    for filename, document in zip(student_file, preprocessed_docs):
        print(f"File: {filename}")
        print("Content:")
        print(document)
        print("-" * 30)


check_pliagrism()
