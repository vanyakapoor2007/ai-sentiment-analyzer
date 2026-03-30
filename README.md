# 🤖 AI Sentiment Analyzer

## 📌 Project Description

This project is a machine learning-based web application that analyzes user input text and determines whether the sentiment is **positive** or **negative**. It also provides a confidence score and additional interactive features for better user experience.

---

## 🎯 Key Features

* Sentiment classification (Positive / Negative)
* Confidence score display
* Sentiment history tracking
* Download results as CSV
* Text-to-speech output
* Dark mode toggle
* Sentiment distribution graph
* Character counter
* Clean and modern UI

---

## 🧠 How It Works

1. User enters text
2. Text is cleaned and preprocessed
3. CountVectorizer converts text into numerical features
4. Naive Bayes model predicts sentiment
5. Result and confidence are displayed

---

## 🛠️ Technologies Used

* Python
* Flask
* scikit-learn
* HTML, CSS, JavaScript

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```id="rj8c0n"
git clone https://github.com/your-username/ai-sentiment-analyzer.git
cd ai-sentiment-analyzer
```

### 2. Install Dependencies

```id="oz8lbz"
pip install flask scikit-learn
```

### 3. Run Application

```id="jzq2cn"
python app.py
```

### 4. Open in Browser

```id="63a6mc"
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```id="6o6y7v"
ai-sentiment-analyzer/
│── app.py
│── model.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 📖 Usage Guide

* Enter text in the input box
* Click **Analyze**
* View sentiment and confidence
* Use additional features like:

  * History tracking
  * Download results
  * Dark mode
  * Graph visualization

---

## ⚠️ Limitations

* Small dataset
* Only positive/negative classification
* Limited accuracy for complex sentences

---

## 🚀 Future Enhancements

* Larger datasets
* Neutral sentiment detection
* Deployment on cloud
* Multi-language support

---

## 👩‍💻 Author

This project was developed as part of the BYOP (Bring Your Own Project) requirement to demonstrate practical application of AI and machine learning concepts.
