import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import time

# --- PENGATURAN HALAMAN ---
st.set_page_config(
    page_title="Deteksi Penipuan Finansial",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNGSI UNTUK MEMUAT MODEL ---
@st.cache_resource
def load_model(model_name):
    """Memuat model machine learning berdasarkan nama yang dipilih."""
    model_filename = f"best_{model_name.lower().replace(' ', '_')}_model.pkl"
    if os.path.exists(model_filename):
        model = joblib.load(model_filename)
        return model, model_filename
    else:
        return None, model_filename

# --- JUDUL APLIKASI ---
st.title("Aplikasi Deteksi Penipuan Finansial 💳")
st.markdown("Gunakan aplikasi ini untuk memprediksi potensi penipuan transaksi menggunakan beberapa model Machine Learning.")

# --- SIDEBAR PENGATURAN ---
st.sidebar.header("⚙️ Pengaturan & Input")
model_option = st.sidebar.selectbox(
    "Pilih Model Machine Learning:",
    ("XGBoost", "Random Forest", "Logistic Regression")
)

# Muat model yang dipilih
model, required_file = load_model(model_option)

# --- ISI UTAMA APLIKASI ---
if model is None:
    st.error(f"Model '{model_option}' tidak ditemukan. Pastikan Anda telah menjalankan `main_lanjutan.py` dan file **'{required_file}'** ada di folder yang sama.")
else:
    st.success(f"Model **'{model_option}'** berhasil dimuat.")
    
    # Definisikan nama fitur
    feature_names = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                     'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
                     'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28',
                     'NormalizedAmount', 'NormalizedTime']

    st.sidebar.markdown("---")
    st.sidebar.header("Input Fitur Transaksi")
    st.sidebar.info("Geser slider untuk mengubah nilai fitur anomali utama.")

    # Fungsi input pengguna
    def user_input_features():
        v14 = st.sidebar.slider('Fitur V14', -20.0, 5.0, -2.5, key='v14')
        v12 = st.sidebar.slider('Fitur V12', -20.0, 5.0, -5.0, key='v12')
        v10 = st.sidebar.slider('Fitur V10', -25.0, 10.0, -3.0, key='v10')
        v17 = st.sidebar.slider('Fitur V17', -26.0, 10.0, -0.5, key='v17')
        v4 = st.sidebar.slider('Fitur V4', -5.0, 17.0, 4.0, key='v4')
        
        feature_array = np.zeros(30)
        feature_array[3] = v4
        feature_array[9] = v10
        feature_array[11] = v12
        feature_array[13] = v14
        feature_array[16] = v17

        input_data = pd.DataFrame(feature_array.reshape(1, -1), columns=feature_names)
        return input_data

    input_df = user_input_features()

    # Membuat Tab
    tab1, tab2 = st.tabs(["📊 Prediksi Interaktif", "ℹ️ Tentang Aplikasi"])

    with tab1:
        st.header("Input Fitur")
        st.write("Berikut adalah nilai fitur yang Anda masukkan melalui sidebar:")
        st.dataframe(input_df[['V4', 'V10', 'V12', 'V14', 'V17']])
        
        if st.sidebar.button('Prediksi Status Transaksi', type="primary", use_container_width=True):
            with st.spinner('Sedang menganalisis transaksi... 🧠'):
                time.sleep(1) # Simulasi proses analisis
                prediction = model.predict(input_df)
                prediction_proba = model.predict_proba(input_df)

            st.header(f"Hasil Prediksi dari Model '{model_option}'")
            col1, col2 = st.columns(2)

            with col1:
                if prediction[0] == 1:
                    st.error("**POTENSI PENIPUAN**", icon="🚨")
                else:
                    st.success("**TRANSAKSI AMAN**", icon="✅")
            
            with col2:
                if prediction[0] == 1:
                    prob_value = prediction_proba[0][1]
                    st.metric(label="Tingkat Keyakinan (Penipuan)", value=f"{prob_value:.2%}", delta="Risiko Tinggi", delta_color="inverse")
                else:
                    prob_value = prediction_proba[0][0]
                    st.metric(label="Tingkat Keyakinan (Aman)", value=f"{prob_value:.2%}", delta="Risiko Rendah", delta_color="off")
    
    with tab2:
        st.header("Tentang Aplikasi Deteksi Penipuan")
        st.markdown("""
        Aplikasi ini adalah prototipe yang dirancang untuk mendemonstrasikan bagaimana Machine Learning dapat digunakan untuk mendeteksi transaksi finansial yang mencurigakan secara *real-time*.

        ### Model yang Digunakan:
        Anda dapat memilih salah satu dari tiga model yang telah dilatih:
        - **Logistic Regression**: Model *baseline* yang cepat dan mudah diinterpretasikan.
        - **Random Forest**: Model *ensemble* yang kuat dan akurat, dibangun dari banyak pohon keputusan.
        - **XGBoost**: Model *Gradient Boosting* yang canggih dan seringkali memberikan performa terbaik untuk data tabular.

        ### Proses Kerja:
        1. **Input**: Pengguna memasukkan beberapa nilai fitur transaksi yang paling berpengaruh.
        2. **Prediksi**: Model yang dipilih akan menganalisis input untuk menentukan probabilitas penipuan.
        3. **Output**: Hasil ditampilkan secara jelas, apakah transaksi aman atau berpotensi penipuan, beserta tingkat keyakinan model.
        """)