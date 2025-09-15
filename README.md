# Sistem Deteksi Penipuan Transaksi Finansial Berbasis Machine Learning 💳

![Project Banner](https://i.imgur.com/8a2eJ2c.png)

<p align="center">
  <img src="https://img.shields.io/badge/status-selesai-brightgreen?style=for-the-badge" alt="Project Status">
  <img src="https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

## 📝 Deskripsi Umum

Aplikasi web ini adalah sebuah prototipe fungsional yang mendemonstrasikan kekuatan *machine learning* untuk mengidentifikasi transaksi kartu kredit yang berpotensi penipuan secara *real-time*. Dengan antarmuka yang interaktif dan responsif, pengguna dapat membandingkan performa dari tiga model klasifikasi yang berbeda dan melihat bagaimana mereka menganalisis transaksi baru. Proyek ini mencakup seluruh alur kerja sains data, mulai dari pra-pemrosesan data hingga *deployment* model dalam sebuah aplikasi web yang mudah digunakan.

---

## 🚀 Fitur Utama

-   **🤖 Perbandingan Tiga Model**: Pengguna dapat secara dinamis memilih dan menggunakan salah satu dari tiga model *machine learning* yang telah dilatih: **XGBoost**, **Random Forest**, dan **Logistic Regression**.
-   **📊 Prediksi Interaktif**: Masukkan nilai fitur-fitur transaksi yang paling berpengaruh menggunakan *slider* untuk mendapatkan prediksi instan beserta tingkat keyakinan model.
-   **📈 Umpan Balik Visual**: Hasil prediksi disajikan dengan jelas menggunakan metrik visual dan kode warna (hijau untuk 'Aman', merah untuk 'Penipuan') untuk interpretasi yang cepat.
-   **⚙️ Pelatihan & Tuning**: Skrip pelatihan (`main_lanjutan.py`) mencakup teknik canggih seperti **SMOTE** untuk menangani data tidak seimbang dan **GridSearchCV** untuk optimasi *hyperparameter*.
-   **✨ UI/UX Modern**: Dibangun dengan Streamlit menggunakan tata letak multi-kolom dan tab untuk pengalaman pengguna yang bersih dan terstruktur.

---

## 🛠️ Tumpukan Teknologi (Technology Stack)

-   **Bahasa Pemrograman**: Python 3.9
-   **Analisis & Model ML**:
    -   Pandas & NumPy (Manipulasi Data)
    -   Scikit-learn (Logistic Regression, Random Forest, GridSearchCV)
    -   XGBoost (Gradient Boosting)
    -   Imbalanced-learn (SMOTE)
-   **Aplikasi Web & UI**: Streamlit
-   **Lingkungan**: Anaconda (Conda)
-   **Dataset**: [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) dari Kaggle.

---

## 📂 Struktur Proyek

```
fraud-detection-project/
│
├── 📄 app.py                 # Skrip utama untuk aplikasi web Streamlit
├── 📄 main_lanjutan.py       # Skrip untuk melatih dan menyimpan model
├── 📄 requirements.txt       # Daftar library yang dibutuhkan (opsional)
├── 📄 README.md              # Dokumentasi proyek (file ini)
├── 📄 .gitignore             # File untuk mengabaikan file yang tidak perlu
│
├── 📁 data/
│   └── 📄 creditcard.csv     # Dataset (diletakkan di sini, diabaikan oleh .gitignore)
│
└── 📁 models/
    ├── 📄 best_xgboost_model.pkl
    ├── 📄 best_random_forest_model.pkl
    └── 📄 best_logistic_regression_model.pkl
    (File-file model diabaikan oleh .gitignore)
```

---

## 🏃‍♀️ Panduan Instalasi & Menjalankan Lokal

Untuk menjalankan aplikasi ini di komputer Anda, ikuti langkah-langkah berikut:

### 1. **Prasyarat**
-   Pastikan Anda telah menginstal **Anaconda/Miniconda** dan **Git**.

### 2. **Clone Repositori**
Buka terminal dan jalankan perintah berikut untuk mengunduh proyek:
```bash
git clone [https://github.com/NAMA_USER_ANDA/NAMA_REPO_ANDA.git](https://github.com/NAMA_USER_ANDA/NAMA_REPO_ANDA.git)
cd NAMA_REPO_ANDA
```

### 3. **Siapkan Lingkungan Anaconda**
Buat dan aktifkan lingkungan virtual baru untuk proyek ini. Ini akan mengisolasi semua dependensi.
```bash
conda create --name fraud_detection python=3.9
conda activate fraud_detection
```

### 4. **Instal Library yang Dibutuhkan**
Instal semua library yang diperlukan menggunakan `pip`.
```bash
pip install streamlit pandas numpy scikit-learn xgboost imbalanced-learn
```

### 5. **Unduh Dataset & Latih Model**
-   Unduh dataset dari **[Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)** dan simpan `creditcard.csv` di dalam folder proyek.
-   Jalankan skrip pelatihan untuk membuat file model `.pkl`. Proses ini mungkin memakan waktu lama.
```bash
python main_lanjutan.py
```

### 6. **Jalankan Aplikasi Web**
Setelah model berhasil dibuat, jalankan aplikasi Streamlit!
```bash
streamlit run app.py
```
Aplikasi sekarang akan terbuka secara otomatis di browser Anda.

---

## 💡 Cara Menggunakan Aplikasi

1.  **Pilih Model**: Di sidebar kiri, pilih salah satu dari tiga model yang tersedia dari menu *dropdown*.
2.  **Masukkan Data**: Gunakan *slider* untuk mengatur nilai dari lima fitur transaksi yang paling berpengaruh.
3.  **Dapatkan Prediksi**: Klik tombol **"Prediksi Status Transaksi"**.
4.  **Lihat Hasil**: Hasil prediksi akan muncul di area utama, lengkap dengan status ('Aman' atau 'Penipuan') dan metrik tingkat keyakinan.
5.  **Eksplorasi**: Coba gunakan model yang berbeda atau nilai input yang bervariasi untuk melihat bagaimana hasilnya berubah.

---