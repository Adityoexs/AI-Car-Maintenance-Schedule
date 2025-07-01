# requirements: streamlit pandas matplotlib scikit-learn textblob transformers torch nltk

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from textblob import TextBlob
from transformers import pipeline
from deep_translator import GoogleTranslator
import nltk

nltk.download('punkt')

# ---------- Class & Data Structure ----------

class VehicleMaintenance:
    def __init__(self, vehicle_type, year, last_odometer, daily_usage, last_service_date):
        self.vehicle_type = vehicle_type
        self.year = year
        self.last_odometer = last_odometer
        self.daily_usage = daily_usage
        self.last_service_date = pd.to_datetime(last_service_date)
        self.history = []
        self.add_service(self.last_service_date, self.last_odometer)
    
    def add_service(self, date, odometer):
        self.history.append({'date': pd.to_datetime(date), 'odometer': odometer})

    def get_history_df(self):
        if not self.history:
        # Return empty DataFrame dengan kolom yang fix
            return pd.DataFrame(columns=['date', 'odometer', 'days_since_last', 'km_since_last'])
        df = pd.DataFrame(self.history)
        if 'date' not in df.columns:
            # Force column name to be right
            df['date'] = pd.NaT
            df = df.sort_values('date')
        if len(df) > 1:
            df['days_since_last'] = (df['date'] - df['date'].shift(1)).dt.days.fillna(0)
            df['km_since_last'] = df['odometer'].diff().fillna(0)
        else:
            df['days_since_last'] = 0
            df['km_since_last'] = 0
        return df.reset_index(drop=True)


    def predict_next_service(self):
        df = self.get_history_df()
        X = df.index.values.reshape(-1, 1)
        y = df['odometer'].values
        model = LinearRegression()
        model.fit(X, y)
        next_index = [[len(df)]]
        predicted_odometer = int(model.predict(next_index)[0])
        avg_days = int(df['days_since_last'][1:].mean()) if len(df) > 1 else 180
        predicted_date = df['date'].iloc[-1] + timedelta(days=avg_days)
        return predicted_odometer, predicted_date

    def visualize(self):
        df = self.get_history_df()
        predicted_odometer, predicted_date = self.predict_next_service()
        fig, ax = plt.subplots()
        ax.plot(df['date'], df['odometer'], marker='o', label='Riwayat Servis')
        ax.axhline(predicted_odometer, color='r', linestyle='--', label='Prediksi Odometer Servis')
        ax.axvline(predicted_date, color='g', linestyle='--', label='Prediksi Tanggal Servis')
        ax.legend()
        ax.set_xlabel("Tanggal Servis")
        ax.set_ylabel("Odometer (km)")
        ax.set_title("Riwayat & Prediksi Servis")
        ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%Y'))
        fig.autofmt_xdate(rotation=45)
        ax.margins(x=0.1)
        st.pyplot(fig)

    def delete_service(self, date):
        date = pd.to_datetime(date)
        self.history = [h for h in self.history if h['date'] != date]


# ---------- AI & NLP Integration ----------

@st.cache_resource
def load_huggingface_pipelines():
    sentiment_pipe = pipeline("sentiment-analysis")
    zero_shot_pipe = pipeline("zero-shot-classification",
                              model="facebook/bart-large-mnli")
    return sentiment_pipe, zero_shot_pipe

sentiment_pipe, zero_shot_pipe = load_huggingface_pipelines()

def analyze_feedback(feedback):
    tb = TextBlob(feedback)
    st.write("**{{Preview Untuk Dikirim ke Database}}**")
    st.write("**Analisis Sentimen (TextBlob):**", tb.sentiment)
    st.write("**Analisis Sentimen (HuggingFace BART):**", sentiment_pipe(feedback))

    candidate_labels = ['oil change', 'brake issue', 'service complaint', 'positive experience',]
    zshot = zero_shot_pipe(feedback, candidate_labels)
    st.write("**Zero-shot Intent Classification:**")
    st.json(zshot)

# ---------- Streamlit UI ----------

st.title("AI Car Maintenance Schedule")

st.header("Input Data Kendaraan")
with st.form("vehicle_form", clear_on_submit=False):
    vehicle_type = st.selectbox("Jenis Kendaraan", ["Sedan", "SUV", "MPV", "Motor", "Lainnya"])
    year = st.number_input("Tahun Pembuatan", min_value=1990, max_value=datetime.now().year, value=2020)
    last_odometer = st.number_input("Odometer Saat Ini (km)", min_value=0, value=35000)
    daily_usage = st.number_input("Rata-rata Pemakaian Harian (km)", min_value=0, value=40)
    last_service_date = st.date_input("Tanggal Servis Terakhir", value=datetime.now() - timedelta(days=90))
    submitted = st.form_submit_button("Simpan Data")

if 'vehicle' not in st.session_state:
    st.session_state.vehicle = None

if submitted:
    st.session_state.vehicle = VehicleMaintenance(
        vehicle_type, year, last_odometer, daily_usage, last_service_date
    )
    st.success("Data kendaraan disimpan.")

if st.session_state.vehicle:
    vehicle = st.session_state.vehicle

    st.header("Tambah Riwayat Servis Baru")
    with st.form("add_service"):
        new_service_date = st.date_input("Tanggal Servis Baru", value=datetime.now())
        new_odometer = st.number_input("Odometer Servis Baru (km)", min_value=0, value=vehicle.last_odometer+5000)
        add_service_btn = st.form_submit_button("Tambah Servis")
    if add_service_btn:
        df_history = vehicle.get_history_df()
        tanggal_baru = pd.to_datetime(new_service_date)
        odometer_baru = new_odometer

        # Handle jika DataFrame belum berisi data valid
        if len(df_history) > 0:
            max_tanggal = df_history['date'].max()
            max_odometer = df_history['odometer'].max()
        else:
            max_tanggal = None
            max_odometer = None

        if tanggal_baru in list(df_history['date']):
            st.error("Tanggal servis sudah ada di riwayat! Silakan pilih tanggal lain.")
        elif max_tanggal is not None and isinstance(max_tanggal, pd.Timestamp) and tanggal_baru < max_tanggal:
            st.error("Tanggal servis tidak boleh lebih awal dari servis terakhir.")
        elif max_odometer is not None and odometer_baru < max_odometer:
            st.error("Odometer tidak boleh lebih kecil dari data terakhir.")
        else:
            vehicle.add_service(new_service_date, new_odometer)
            st.success("Servis baru ditambahkan.")
            st.rerun()

    # --- Bagian ini selalu tampil ---
    st.subheader("Riwayat Servis Kendaraan")
    df_history = vehicle.get_history_df()

    # Tabel DataFrame lengkap
    st.dataframe(df_history[['date', 'odometer', 'km_since_last', 'days_since_last']])

    # Setelah st.dataframe(...)
    if len(df_history) == 0:
        st.info("Belum ada riwayat servis.")
    else:
        # List dengan tombol hapus
        for idx, row in df_history.iterrows():
            col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])
            with col1:
                st.write(row['date'].strftime('%Y-%m-%d'))
            with col2:
                st.write(int(row['odometer']))
            with col3:
                st.write(int(row['km_since_last']))
            with col4:
                st.write(int(row['days_since_last']))
            with col5:
                if st.button("Hapus", key=f"hapus_{idx}"):
                    vehicle.delete_service(row['date'])
                    st.success(f"Riwayat servis pada {row['date'].strftime('%Y-%m-%d')} dihapus.")
                    st.rerun()

        pred_odometer, pred_date = vehicle.predict_next_service()
        st.info(f"**Prediksi servis berikutnya:** {pred_date.strftime('%Y-%m-%d')} / {pred_odometer:,} km")

        vehicle.visualize()

        if datetime.now().date() > pred_date.date():
            st.error("Jadwal servis sudah lewat, segera lakukan perawatan!")
        else:
            st.success("Jadwal servis masih sesuai.")

        st.header("Masukkan Feedback/Keluhan Anda (Opsional)")
        feedback = st.text_area("Tulis pengalaman atau keluhan servis:")
        if st.button("Analisis Feedback"):
            translated = GoogleTranslator(source='auto', target='en').translate(feedback)
            analyze_feedback(translated)
else:
    st.info("Silakan input dan simpan data kendaraan terlebih dahulu.")



st.caption("Made with Streamlit, Scikit-Learn, Hugging Face Transformers, TextBlob, Matplotlib, Pandas, OOP Python.")

