import pandas as pd
import re

df = pd.read_csv("stopwords.csv")


def preprocess_text(text):
    amharic_stopwords = df["stopword"].tolist()
    amharic_punctuation = "።፣፤፥፦፧፨.,?!"

    tokens = text.split(" ")

    tokens = [
        re.sub(f"[{re.escape(amharic_punctuation)}]", "", word)
        for word in tokens
        if word not in amharic_stopwords
    ]
    preprocessed_text = " ".join(tokens)

    return preprocessed_text
