## 📄 README.md

# Medical Insurance Cost Prediction Dashboard

![Build Status](https://github.com/the-first-lady/REPO/actions/workflows/python-app.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-dashboard-orange.svg)

Dashboard ini dibuat dengan **Streamlit** untuk memprediksi biaya asuransi kesehatan menggunakan model **XGBoost**.  
Selain prediksi, dashboard juga menampilkan interpretasi model dengan **SHAP**.

---

## 🚀 Setup Environment

1. **Clone / buka folder proyek**
   ```bash
   cd Project_Python/Medical Insurance Cost Prediction
   ```

2. **Buat environment baru (opsional, lebih aman)**
   ```bash
   conda create -n insurance_env python=3.9
   conda activate insurance_env
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Menjalankan Dashboard

Jalankan perintah berikut dari folder proyek:
```bash
streamlit run dashboard_medical_insurance.py
```

Dashboard akan terbuka di browser pada alamat:
```
http://localhost:8501
```

---

## 🛑 Menonaktifkan Environment

Jika menggunakan **conda**:
```bash
conda deactivate
```

Jika menggunakan **venv** (virtualenv bawaan Python):
```bash
deactivate
```

---

## 📂 Struktur Proyek

```
Medical Insurance Cost Prediction/
│
├── Dashboard Medical Insurance Cost Prediction/
│   └── dashboard_medical_insurance.py       # Script utama Streamlit
│   └── requirements.txt                     # Daftar dependencies
│   └── README.md                            # Dokumentasi proyek
│   └── xgboost_model.pkl                    # File model tersimpan
├── Medical Insurance Cost Prediction.ipynb
├── medical-charges.csv

---

## 📸 Contoh Tampilan

### Input Form
Pengguna memasukkan data seperti:
- Age: 35  
- BMI: 27.5  
- Children: 2  
- Smoker: No  
- Region: Northwest  

### Output Prediksi
- **Predicted Insurance Cost:** \$12,345  

### Visualisasi SHAP
Grafik SHAP menampilkan kontribusi fitur:
- **Smoker** → faktor terbesar menaikkan biaya  
- **BMI** → berpengaruh sedang  
- **Children** → pengaruh kecil  

---

## ✨ Catatan
- Pastikan file `xgboost_model.pkl` ada di folder proyek.
- Jika ada error versi library, gunakan environment baru agar lebih stabil.
```
