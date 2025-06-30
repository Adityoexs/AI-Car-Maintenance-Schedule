# 🚗 AI Car Maintenance Schedule – Streamlit App

![Aplikasi Preview](preview.png)

Aplikasi **AI Car Maintenance Schedule** ini adalah platform berbasis Streamlit untuk pencatatan, analisis, dan prediksi servis kendaraan berbasis data odometer & histori servis.  
Aplikasi ini juga terintegrasi dengan AI/NLP untuk analisis sentimen & klasifikasi keluhan secara otomatis.

---

## 📦 Fitur Utama

- **Input Data Kendaraan**: Simpan jenis kendaraan, tahun, odometer, dan histori servis awal.
- **Tambah Riwayat Servis**: Catat servis baru secara periodik (tanggal dan odometer).
- **Table + Pagination**: Lihat riwayat servis dalam bentuk tabel rapi (dengan pagination).
- **Prediksi Jadwal Servis**: Prediksi otomatis kapan kendaraan perlu servis berikutnya (berdasarkan tren historis).
- **Visualisasi Interaktif**: Grafik tren servis dan odometer per tanggal.
- **AI/NLP Feedback**: Analisis sentimen dan klasifikasi keluhan secara otomatis (TextBlob & Hugging Face).
- **Proteksi Data**: Riwayat servis pertama tidak dapat dihapus untuk mencegah kehilangan anchor data.

---

## 🖼️ Preview UI

![Preview Streamlit App](preview.png)

---

## 🚀 Cara Menjalankan Aplikasi

1. **Kloning repo & masuk folder**
    ```bash
    git clone https://github.com/username/ai-car-maintenance.git
    cd ai-car-maintenance
    ```

2. **Buat dan aktifkan virtual environment (opsional)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. **Install dependensi**
    ```bash
    pip install -r requirements.txt
    ```
    > **Atau install manual:**  
    > `pip install streamlit pandas matplotlib scikit-learn textblob transformers torch nltk deep-translator`

4. **Jalankan aplikasi**
    ```bash
    streamlit run app.py
    ```

---

## 🛠️ Instruksi Penggunaan

1. **Input Data Kendaraan**  
   Masukkan jenis kendaraan, tahun, odometer terakhir, dan tanggal servis terakhir lalu klik "Simpan Data".

2. **Tambah Riwayat Servis Baru**  
   Setelah data kendaraan disimpan, tambahkan histori servis baru secara periodik melalui form yang tersedia.

3. **Lihat & Kelola Riwayat Servis**  
   Tabel riwayat servis tampil otomatis.  
   Gunakan tombol **Prev/Next** untuk navigasi halaman jika riwayat panjang.  
   Tanggal servis paling awal (anchor) tidak bisa dihapus.

4. **Prediksi & Visualisasi**  
   Lihat prediksi jadwal servis berikutnya dan grafik tren servis langsung di bawah tabel.

5. **Analisis Feedback/Komplain**  
   Masukkan keluhan atau feedback pada field yang tersedia, klik “Analisis Feedback” untuk melihat hasil analisis AI (sentimen, intent, dsb).

---

## 🧰 Library & Model AI/ML yang Digunakan

- **Streamlit**: Framework web Python interaktif.
- **Pandas**: Manajemen & manipulasi data tabular.
- **Matplotlib**: Visualisasi grafik tren data.
- **Scikit-learn**: Model prediksi linear.
- **TextBlob**: Analisis sentimen teks.
- **Transformers (Hugging Face)**: Sentiment analysis, zero-shot classification.
- **Torch**: Backend AI/NLP.
- **NLTK**: Pre-processing text.
- **Deep Translator**: Translasi feedback user.
- **Model**: BART, zero-shot, dst (bisa ditambah).

---

## 📝 Catatan

- Data kendaraan dan histori servis **hanya tersimpan selama sesi berjalan** (belum ada database).
- Aplikasi bisa dengan mudah di-deploy ke **Streamlit Cloud** atau VPS/hosting sendiri.
- **Screenshot** bisa diganti dengan hasil aplikasimu sendiri (`preview.png`).

---

> Dibuat oleh Adityo Eko Saputro, 2025  
> Powered by Python, Streamlit, & Hugging Face NLP

