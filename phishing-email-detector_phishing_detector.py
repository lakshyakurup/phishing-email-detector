import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample Email Dataset (Phishing = 1, Legitimate = 0)
data = {
    'text': [
        "Urgent: Your account has been suspended! Click here to restore access immediately.",
        "Hey, are we still meeting for lunch today at 12:30?",
        "Security Alert: Unusual login detected. Verify your password now.",
        "Please find attached the updated project timeline for next week.",
        "Congratulations! You won a $1,000 gift card. Claim your prize now!",
        "Can you review the attached document and let me know your thoughts?"
    ],
    'label': [1, 0, 1, 0, 1, 0]
}

def main():
    print("=====================================================")
    print("      PHISHING EMAIL DETECTION MACHINE LEARNING      ")
    print("=====================================================")

    # 1. Load Data into DataFrame
    df = pd.DataFrame(data)
    print("\n[+] Sample Dataset Loaded:")
    print(df[['text', 'label']])

    # 2. Features and Target
    X = df['text']
    y = df['label']

    # 3. Train / Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4. Text Vectorization (CountVectorizer)
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # 5. Model Initialization & Training (Naive Bayes)
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    # 6. Evaluation
    y_pred = model.predict(X_test_vec)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"\n[+] Model Accuracy: {acc * 100:.2f}%")
    print("\n--- Classification Report ---")
    print(classification_report(y_test, y_pred, target_names=['Legitimate (0)', 'Phishing (1)'], zero_division=0))

    # 7. Interactive Prediction Testing
    print("\n=====================================================")
    print("             TEST CUSTOM EMAIL TEXT                 ")
    print("=====================================================")
    sample_inputs = [
        "URGENT: Verify your bank login credentials now to prevent block!",
        "Hi Team, attached is the presentation for tomorrow's meeting."
    ]

    for sample in sample_inputs:
        sample_vec = vectorizer.transform([sample])
        pred = model.predict(sample_vec)[0]
        status = "PHISHING EMAIL (1)" if pred == 1 else "LEGITIMATE EMAIL (0)"
        print(f"\nEmail Content: \"{sample}\"")
        print(f"Prediction   : {status}")

if __name__ == "__main__":
    main()
