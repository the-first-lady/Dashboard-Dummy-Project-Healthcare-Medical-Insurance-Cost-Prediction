``markdown
# 🏥 Medical Insurance Cost Prediction

Dashboard interaktif berbasis **Streamlit** untuk memprediksi biaya asuransi kesehatan menggunakan model **XGBoost Regressor**.

## 🚀 Demo Aplikasi
Klik untuk mencoba langsung di Streamlit Cloud:  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/the-first-lady/Medical-Insurance-Cost-Prediction/main/dashboard_medical_insurance.py)

--

## 📂 Struktur Repo
``
Medical-Insurance-Cost-Prediction/
├── dashboard_medical_insurance.py   # Dashboard Streamlit
├── xgboost_model.pkl                # Model hasil training
├── requirements.txt                 # Daftar library
└── README.md                        # Dokumentasi project
``
## ⚙️ Cara Menjalankan di Lokal
1. Clone repo:
   ```bash
   git clone https://github.com/the-first-lady/Medical-Insurance-Cost-Prediction.git
   cd Medical-Insurance-Cost-Prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan dashboard:
   ```bash
   streamlit run dashboard_medical_insurance.py
   ```

---

## 📊 Model
- Algoritma: **XGBoost Regressor**
- Library utama: `scikit-learn`, `xgboost`, `joblib`
- Model dilatih di notebook (`.ipynb`) lalu disimpan sebagai `xgboost_model.pkl`.

---

## ✨ Fitur Dashboard
- Input interaktif: usia, BMI, jumlah anak, status merokok, jenis kelamin.
- Prediksi biaya asuransi kesehatan secara real-time.
- Visualisasi hasil dengan antarmuka Streamlit yang sederhana.

---

## 📌 Catatan
- Training model dilakukan di notebook, bukan di dashboard.
- Dashboard hanya **load model** untuk inference → startup lebih cepat dan stabil.
```

---

Dengan README ini:
- Orang lain bisa langsung klik badge untuk membuka dashboard di Streamlit Cloud.  
- Struktur repo jelas.  
- Instruksi instalasi lokal tersedia.  
- Penjelasan model dan fitur singkat ada.  
