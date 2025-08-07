import joblib
import speech_recognition as sr
import matplotlib.pyplot as plt

# Load the saved model and vectorizer
model = joblib.load('sentiment_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

def pred(input_review):
    input_review_tfidf = vectorizer.transform([input_review])
    predicted_sentiment = model.predict(input_review_tfidf)[0]
    predicted_probabilities = model.predict_proba(input_review_tfidf)[0]
    return predicted_sentiment, predicted_probabilities


def analyze_text(input_text):
    input_text_tfidf = vectorizer.transform([input_text])
    predicted_sentiment = model.predict(input_text_tfidf)[0]
    predicted_probabilities = model.predict_proba(input_text_tfidf)[0]
    return predicted_sentiment, predicted_probabilities

def analyze_audio(audio_path):
    try:
        r = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
        transcribed_text = r.recognize_google(audio)
        sentiment, probabilities = analyze_text(transcribed_text)
        return transcribed_text, sentiment, probabilities
    except Exception as e:
        return str(e), None, None