from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "this is a sentence",
    "this sentence is another sentence"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

print(vectorizer.get_feature_names_out())
print(X.toarray())
