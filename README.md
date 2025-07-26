# 📧 Email Spam Classifier

This project uses **machine learning and natural language processing** to classify emails as **Spam** or **Ham (Not Spam)**. It includes a **Streamlit web interface** where users can paste email content and get predictions in real time.

---

## 🔍 How It Works

- Emails are vectorized using `TfidfVectorizer`
- Model is trained using `LogisticRegression`
- Input text is transformed and classified live using Streamlit

---

## 📸 Example Inputs

<table>
  <tr>
    <td align="center"><b>✅ Ham Email</b></td>
    <td align="center"><b>⚠️ Spam Email</b></td>
  </tr>
  <tr>
    <td>
      <img src="Screenshot%202025-07-26%20223311.png" width="100%" alt="Ham Example">
    </td>
    <td>
      <img src="Screenshot%202025-07-26%20223449.png" width="100%" alt="Spam Example">
    </td>
  </tr>
</table>

---

## 🚀 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

---

## 🛠️ How to Run Locally

1. Clone the repository  
   git clone https://github.com/TusharKotian/Email-Spam-Classifier.git
   cd Email-Spam-Classifier
2. Install Dependencies
    pip install -r requirements.txt
3. Run the App
    streamlit run app.py
