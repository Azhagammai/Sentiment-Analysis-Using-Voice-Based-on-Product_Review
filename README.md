
# 🎤 Voice-Based Sentiment Analysis on Product Reviews

## 📌 Overview  
This project is a **Voice-Based Sentiment Analysis System** that accepts voice inputs from users, converts them to text, and classifies the sentiment as **Positive**, **Negative**, or **Neutral** using a machine learning model trained on e-commerce review data.

---

## 🚀 Features  
- 🎙 Accepts voice input (`.wav` files)  
- 🧼 Preprocessing & TF-IDF vectorization  
- 🤖 Sentiment classification using ML  
- 🌐 Web interface with HTML/CSS  
- 📊 Trained using real-world product review dataset  

---

## 📁 Project Folder Structure  

```
Project/
├── backend.html                          # Web interface
├── sentiment_model.joblib                # Pre-trained sentiment model
├── tfidf_vectorizer.joblib               # TF-IDF vectorizer
└── app/
    ├── analyze.py                        # Main sentiment analyzer
    ├── output.py                         # Output logic
    ├── model.ipynb                       # Jupyter Notebook for training
    ├── test.wav                          # Sample voice input
    ├── Womens Clothing E-Commerce Reviews.csv  # Dataset
    └── static/
        ├── css/                          # Stylesheets
        └── pics/                         # Images for UI
```

---

## 🛠 Tech Stack  

| Layer       | Tools Used                      |
|-------------|----------------------------------|
| Frontend    | HTML, CSS (Bootstrap)           |
| Backend     | Python                          |
| ML Model    | Scikit-learn, Joblib            |
| Data Prep   | Numpy, Pandas                   |
| Notebook    | Jupyter                         |

---

## 📦 Dependencies  

Install the required libraries using:

```bash
pip install numpy pandas scikit-learn joblib
```

---

## 🧪 Step-by-Step Guide to Run the Project

### 1️⃣ Prerequisites

Make sure you have:
- Python 3.7 or higher  
- `pip`  
- Jupyter Notebook (optional)

---

### 2️⃣ Install Libraries  

Open terminal and run:

```bash
pip install numpy pandas scikit-learn joblib
```

---

### 3️⃣ Run the Analyzer  

Navigate to the working folder:

```bash
cd Project/app
python analyze.py
```

This will:
- Load the `.joblib` model and vectorizer  
- Convert `test.wav` into text  
- Predict and print the sentiment  

---

### 4️⃣ Open Web Interface  

Open this file in any browser:

```
Project/backend.html
```

✅ This will show a basic UI for user input.

---

### 5️⃣ (Optional) Retrain Model  

Open and explore the training logic:

```bash
cd Project/app
jupyter notebook model.ipynb
```

---

## ✅ Output  

The model outputs one of the following:
- `Positive`  
- `Negative`  
- `Neutral`

Displayed either in terminal or in the browser (if integrated).

---

## 📂 Detailed File Descriptions

| File/Folder                             | Description                                           |
|----------------------------------------|-------------------------------------------------------|
| `backend.html`                         | Frontend interface                                    |
| `sentiment_model.joblib`              | Pre-trained sentiment classifier model                |
| `tfidf_vectorizer.joblib`             | TF-IDF vectorizer for preprocessing                   |
| `app/analyze.py`                      | Core analyzer script (loads audio, predicts)          |
| `app/output.py`                       | Handles display/output of results                     |
| `app/model.ipynb`                     | Model training Jupyter Notebook                       |
| `app/test.wav`                        | Voice sample file for testing                         |
| `app/Womens Clothing E-Commerce Reviews.csv` | Dataset used for training                      |
| `app/static/css/`                     | CSS styling folder                                    |
| `app/static/pics/`                    | UI images used in frontend                            |

---
