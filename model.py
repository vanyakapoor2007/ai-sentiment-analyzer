from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

positive_texts = [
    "i love this product","this is amazing","very good product","excellent work",
    "i am very happy","i like this a lot","people will like it","this is great",
    "fantastic experience","very useful","works perfectly","highly recommend this",
    "i enjoyed this","superb quality","absolutely wonderful","very satisfied",
    "it is awesome","really impressive","brilliant work","nice experience",
    "loved it","best ever","very well done","this is fantastic",
    "great job","i am impressed","very nice product","it is excellent",
    "perfect result","good performance"
]

negative_texts = [
    "i hate this product","this is terrible","very bad product","worst experience ever",
    "i am very unhappy","i dislike this","people will hate it","this is awful",
    "horrible experience","not useful at all","does not work properly","very disappointing",
    "i regret using this","poor quality","absolutely useless","very dissatisfied",
    "it is bad","really disappointing","pathetic service","waste of time",
    "worst ever","not good","very poor performance","extremely bad",
    "terrible quality","completely useless","very frustrating","does not work",
    "awful product","bad experience"
]

texts = positive_texts + negative_texts
labels = ["positive"] * len(positive_texts) + ["negative"] * len(negative_texts)

cleaned_texts = [clean_text(t) for t in texts]

vectorizer = CountVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(cleaned_texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_sentiment(text):
    cleaned = clean_text(text)
    text_vector = vectorizer.transform([cleaned])

    prediction = model.predict(text_vector)[0]
    probability = model.predict_proba(text_vector).max()

    return prediction, round(probability * 100, 2)