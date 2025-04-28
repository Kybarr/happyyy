import streamlit as st
from datetime import datetime
from PIL import Image

# Data Sae
nama = "Sae"
tanggal_lahir = datetime(2004, 4, 25)


# Judul Aplikasi
st.title("🎉 Selamat Ulang Tahun Sae! 🎂")

img = Image.open('Ulangtahun.jpg')
st.image('ulangtahun.jpg')

# Hari ini
today = datetime.today()

# Menghitung usia
usia = today.year - tanggal_lahir.year
if (today.month, today.day) < (tanggal_lahir.month, tanggal_lahir.day):
    usia -= 1

# Menampilkan ucapan
if today.month == tanggal_lahir.month and today.day == tanggal_lahir.day:
    st.success(f"🎉🎂 Selamat ulang tahun {nama} yang ke-{usia}! 🎂🎉")
    st.balloons()
else:
    st.info(f"Hari ini ulang tahun kamu {nama}. Yeyyyyy sekarang berusia {usia} tahun.")
    st.info("お誕生日おめでとう!")
    st.info("Happy Birthday!")

st.title("🎶🎂")

# Menambahkan audio
audio_file = open('Happy Birthday Song!!!.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3', start_time=0)