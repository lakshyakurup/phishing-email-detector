# Phishing Email Detector

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x" />
  <img src="https://img.shields.io/badge/Scikit_Learn-Machine_Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Security-Email_Protection-red?style=for-the-badge" alt="Security" />
</p>

A Machine Learning-based security classification system developed in Python. It analyzes raw email textual content, extracts word frequency features using `CountVectorizer`, and utilizes a `MultinomialNB` (Naive Bayes) model to accurately identify phishing attempts versus legitimate communications.

> **Internship Context:** Developed as part of the **Thiranex Cybersecurity Virtual Internship Program**.

---

## 📌 Features

- **Text Feature Extraction:** Converts raw text into numerical feature matrices using Natural Language Processing (NLP) bag-of-words representation (`CountVectorizer`).
- **Naive Bayes Classification:** Employs `MultinomialNB` to perform probabilistic classification optimized for text detection tasks.
- **Data Pipeline:** Seamlessly handles dataset loading via `pandas`, train-test splitting (`train_test_split`), and evaluation metrics.
- **Model Evaluation:** Calculates accuracy, precision, recall, and F1-score via `scikit-learn`.
- **Interactive Inference:** Evaluates custom email inputs and outputs real-time phishing probability classifications.

---

## ⚙️ Architecture & Dataflow

```
[ Raw Email Data (Text) ]
           │
           ▼
[ Pandas DataFrame Loading ]
           │
           ▼
 [ Train / Test Split (80/20) ]
           │
           ▼
  [ CountVectorizer Feature Extraction ]
           │
           ▼
[ Multinomial Naive Bayes Model Fit ]
           │
           ▼
[ Predictions & Performance Evaluation ]
 (Accuracy, Precision, Recall, F1-Score)
```

---

## 📊 Classifications & Metrics

| Class | Label | Description |
| :--- | :---: | :--- |
| **Legitimate** | `0` | Standard business or personal communications containing benign context. |
| **Phishing** | `1` | Fraudulent attempts containing urgency, credential harvesting, or suspicious links. |

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- **Python 3.x**

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the phishing detection pipeline:
```bash
python phishing_detector.py
```

---

## 🖥️ Terminal Interface Preview

```text
=====================================================
      PHISHING EMAIL DETECTION MACHINE LEARNING      
=====================================================

[+] Sample Dataset Loaded:
                                                text  label
0  Urgent: Your account has been suspended! Clic...      1
1  Hey, are we still meeting for lunch today at ...      0
...

[+] Model Accuracy: 100.00%

--- Classification Report ---
                precision    recall  f1-score   support

Legitimate (0)       1.00      1.00      1.00         1
  Phishing (1)       1.00      1.00      1.00         1

=====================================================
             TEST CUSTOM EMAIL TEXT                 
=====================================================

Email Content: "URGENT: Verify your bank login credentials now to prevent block!"
Prediction   : PHISHING EMAIL (1)

Email Content: "Hi Team, attached is the presentation for tomorrow's meeting."
Prediction   : LEGITIMATE EMAIL (0)
```

---

## 📁 Repository Structure

```text
phishing-email-detector/
│
├── phishing_detector.py    # Main ML pipeline (vectorizer, classifier, evaluator)
├── README.md               # Project documentation & setup instructions
└── requirements.txt        # Required Python libraries
```

---

## 📜 Disclaimer
*This project is designed for educational and defensive cybersecurity purposes as part of machine learning security research.*

Developed for the **Thiranex Cybersecurity Virtual Internship Program**.
