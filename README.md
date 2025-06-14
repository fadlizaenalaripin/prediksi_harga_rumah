# 🎯 Prediksi Harga Rumah dengan Machine Learning

Proyek ini menggunakan algoritma *Linear Regression* untuk memprediksi harga rumah berdasarkan:
- 📏 Luas Rumah (m²)
- 🛏️ Jumlah Kamar Tidur
- 🚿 Jumlah Kamar Mandi

---

## 📁 Struktur Folder
projek_prediksi_harga/
├── data/
│ └── dataset_prediksi_harga_rumah.csv
├── model/
│ └── model_prediksi_harga.pkl
├── plots/
│ ├── prediksi_vs_asli.png
│ ├── korelasi_harga_rumah.png
│ └── distribusi_harga.png
├── README

--

## 🧪 Evaluasi Model

- 🔢 **Metode**: Linear Regression
- 📈 **R² Score**: 0.88
- 🧮 **RMSE**: ±42.5 juta

---

## 🚀 Cara Menggunakan Model

```python
import joblib

model = joblib.load("model/model_prediksi_harga.pkl")
prediksi = model.predict([[80, 3, 2]])  # 80m², 3 kamar tidur, 2 kamar mandi
print(prediksi)


🧠 Tools yang Digunakan
Python

Pandas

Scikit-Learn

Matplotlib & Seaborn


---

