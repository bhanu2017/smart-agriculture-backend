# 🌱 Smart Agriculture Web Application

An intelligent full-stack web application that integrates **Machine Learning and Web Technologies** to assist farmers in **plant disease detection, crop selection, pesticide analysis, and market price insights**.

---

## 📌 Project Overview

This system leverages **Artificial Intelligence** to provide real-time agricultural assistance through:

- 🌿 Disease detection from leaf images  
- 🌾 Smart crop recommendation  
- 🧪 Pesticide safety analysis  
- 💰 Market price tracking  
- 🎤 Voice-based assistant  

---

## 🚀 Key Features

- AI-powered Leaf Disease Detection  
- Crop Recommendation System  
- Pesticide Scanner  
- Market Price Analysis  
- Voice-enabled Smart Assistant  
- Secure Authentication  

---

## 🧠 Machine Learning Model

- Framework: TensorFlow & Keras  
- Architecture: EfficientNetB4 (Transfer Learning)  
- Dataset: ~900MB (61,000+ images)  
- Classes: 39 plant diseases  
- Accuracy: **~92.86%**  

### ⚙️ Training Highlights
- Image size: 160 × 160  
- Data split: 80/10/10  
- Fine-tuning applied  
- Dropout for regularization  

---

## 🛠️ Tech Stack

| Layer        | Technology |
|-------------|-----------|
| Frontend     | HTML, CSS, JavaScript |
| Backend      | Django |
| ML Framework | TensorFlow / Keras |
| Database     | SQLite |
| API          | Django REST Framework |

---

# 📸 Application Screenshots

## 🔐 Signup Page

![image alt](https://github.com/bhanu2017/smart-agriculture-backend/blob/9e54d7617654d37df7c3950ee46f57d35c2220b9/signup.png)

Users can:
- Register securely  
- Create new accounts  

---
## 🔐 Login Page

![image alt](https://github.com/bhanu2017/smart-agriculture-backend/blob/9e54d7617654d37df7c3950ee46f57d35c2220b9/login.png)

Provides:
- Secure login  
- Access to personalized dashboard  

---

## Home Pages


---

## 🌿 Leaf Disease Detection

![Leaf Detection](leaf detection(1).png)

This feature allows users to:
- Upload a leaf image  
- Detect plant diseases instantly  
- View disease name, cause, and cure  

---

## 🌾 Crop Recommendation System

![Crop Selection](crop selection(3).png)

Users can:
- Select soil type  
- Get recommended crops  
- View farming tips and requirements  

---

## 💰 Market Price Analysis

![Market Price](marketprice(2).png)

Displays:
- Crop prices (Min / Max / Modal)  
- Market-specific insights  

---

## 🧪 Pesticide Scanner

![Pesticide Scanner](Pesticide Scanner(1).png)

Allows users to:
- Enter pesticide name  
- View toxicity, safety, and usage  
- Check regulatory status  

---

## 🎤 Smart Agro Dashboard

![Dashboard](Screenshot 2026-03-18 at 8.07.20 AM(1).png)

Main dashboard includes:
- Voice assistant  
- Feature navigation cards  
- Smart farming overview  

---

## 📊 Analytics & Features Overview

![Features](Screenshot 2026-04-18 at 8.31.28 AM(1).png)

Highlights:
- Supported crops  
- Accuracy metrics  
- AI assistance capabilities  

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/bhanu2017/smart-agriculture-backend.git
cd smart-agriculture-backend
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r smart_agro_backend/requirements.txt
```

---

### 4️⃣ Run Server

```bash
python smart_agro_backend/manage.py runserver
```

---

## 🤖 ML Model Setup

- Model is not included due to size  
- Automatically downloads on first run  

### Manual Setup

Download:
https://drive.google.com/uc?id=1OXtoxNMXVZ1pz96avInbV-Tx5DICJF17  

Place inside:

```
smart_agro_backend/ml_models/
```

Rename:

```
plant_disease_recog_model_pwp.keras
```

---

## 📂 Project Structure

```
smart-agriculture-backend/
│
├── smart_agro_backend/
│   ├── accounts/
│   ├── ai/
│   ├── templates/
│   ├── static/
│   ├── ml_models/
│   ├── data/
│   └── manage.py
│
├── .gitignore
└── README.md
```

---

## 🔍 Key Highlights

- Real-world AI application  
- Full-stack + Machine Learning integration  
- Efficient handling of large models  
- Clean and scalable architecture  
- Portfolio-ready project  

---

## 🚀 Future Enhancements

- Cloud deployment (AWS / Render)  
- Mobile-friendly UI  
- Voice assistant improvements  
- Advanced analytics  
- Multi-language support  

---

## 👨‍💻 Author

**Bhanu Prakash**  
GitHub: https://github.com/bhanu2017  

---

## 📌 Conclusion

This project demonstrates how **AI can be effectively integrated into web applications** to solve real-world agricultural problems.

---

🚀 *Empowering Agriculture with AI* 🌱
