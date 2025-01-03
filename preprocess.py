import re


def preprocess_text(text, amharic_stopwords):
    amharic_punctuation = "።፣፤፥፦፧፨.,?!"

    tokens = text.split(" ")

    tokens = [
        re.sub(f"[{re.escape(amharic_punctuation)}]", "", word)
        for word in tokens
        if word not in amharic_stopwords
    ]
    tokens = [token for token in tokens if token.strip()]
    preprocessed_text = " ".join(tokens)

    return preprocessed_text
