# 🚗 AI Car Maintenance Schedule – Streamlit App

![Screenshot 2025-06-30 132525](https://github.com/user-attachments/assets/552fea23-c627-4267-b35b-a2029d3aebdd)

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

![Screenshot 2025-06-30 132525](https://github.com/user-attachments/assets/596d9d6e-876e-4cd1-a67e-918effd1425f)
![Screenshot 2025-06-30 133414](https://github.com/user-attachments/assets/0cd131d3-493e-4a27-aa12-c52a7b22a3c8)
![Screenshot 2025-06-30 133432](https://github.com/user-attachments/assets/f0dbaa4c-e83c-4ea0-b244-4a5983ec6bc0)
![Screenshot 2025-06-30 133439](https://github.com/user-attachments/assets/6fee4eca-a882-4d9a-90e2-506dcf5b3e5f)

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

---

> Dibuat oleh Adityo Eko Saputro, 2025  
> Powered by Python, Streamlit, & Hugging Face NLP

