
# 🎤 Voice-Based Sentiment Analysis on Product Reviews

## 📌 Overview

This project is a **Voice-Based Sentiment Analysis System** that accepts voice inputs from users, converts them to text, and classifies the sentiment as **Positive**, **Negative**, or **Neutral** using a machine learning model trained on e-commerce reviews.

## 🚀 Features

- 🎙️ Accepts voice input (`.wav` files)
- 🧼 Text preprocessing and TF-IDF vectorization
- 🤖 ML-based sentiment classification
- 🌍 Clean web interface for interaction
- 📂 Based on real e-commerce review dataset

## 📁 Folder Structure

```
Project/
├── backend.html
├── sentiment_model.joblib
├── tfidf_vectorizer.joblib
├── app/
│   ├── analyze.py
│   ├── output.py
│   ├── model.ipynb
│   ├── test.wav
│   ├── Womens Clothing E-Commerce Reviews.csv
│   ├── static/
│   │   ├── css/
│   │   └── pics/
```

## 📊 Dataset

- **Name:** Women's Clothing E-Commerce Reviews
- **Source:** Publicly available data
- **Usage:** Used for training and testing sentiment analysis model

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS (Bootstrap)
- **Backend:** Python
- **ML Libraries:** scikit-learn, joblib
- **Others:** Jupyter Notebook, Numpy, Pandas

## 🧪 How to Run

1. Clone the repository and extract the files.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend Python script:
   ```bash
   python analyze.py
   ```
4. Open `backend.html` in a browser to test the UI.

## ✅ Output

- The model predicts sentiment from user voice input.
- Output is displayed in the browser as:
  - **Positive**
  - **Negative**
  - **Neutral**



