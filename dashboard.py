import streamlit as st

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Analisis Polusi Udara di Beijing China (2013-2017)</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>by: Muhammad Wishka Al Hafiidh Suskalanggeng</h6>", unsafe_allow_html=True)

# Pertanyaan 1
st.header("Rumusan Masalah 1: Stasiun mana di Beijing China yang memiliki tingkat PM2.5 dan PM10 yang terendah dalam rentang tahun 2013 hingga 2017?")    
st.subheader("Hasil:")    
st.image("kualitas_udara.png", caption="Grafik Kualitas Udara")
st.write("Berdasarkan data diatas, dalam rentang tahun 2013 hingga 2017, stasiun Dingling memiliki kadar PM2.5 dan PM10 yang paling rendah di antara stasiun-stasiun lainnya di Beijing dalam rentang tahun 2013 hingga 2017")
st.markdown("---")

# Pertanyaan 2
st.header("Rumusan Masalah 2: Dalam rentang tahun 2013 hingga 2017 di antara gas SO2, NO2, CO, dan O3, manakah yang memiliki hubungan korelasi paling kuat terhadap PM2.5 dan PM10 pada stasiun di Beijing China dan bagaimanakah hubungannya?")
st.subheader("Hasil:")
st.image("heatmap_gas.png", caption="Heatmap Korelasi Gas terhadap PM2.5 dan PM10")
st.write("Dalam rentang tahun 2013 hingga 2017, gas yang paling berkorelasi dengan tingginya PM2.5 dan PM10 di stasiun di Beijing China adalah gas CO, dengan nilai korelasi 0.77 terhadap PM2.5 dan 0.69 terhadap PM10")
st.markdown("---")

# Pertanyaan 3
st.header("Rumusan Masalah 3: Dalam rentang tahun 2013 hingga 2017, apakah ada hubungan antara parameter udara seperti temperatur udara, tekanan udara, suhu titik embun, curah hujan, dan kecepatan angin terhadap PM2.5 dan PM10 pada stasiun di Beijing China?")
st.subheader("Hasil:")
st.image("heatmap_udara.png", caption="Heatmap Korelasi Parameter Udara dengan PM2.5 dan PM10")
st.write("Dalam rentang tahun 2013 hingga 2017, pada parameter udara di stasiun di Beijing China, ditemukan semua parameter berkorelasi lemah ataupun tidak berkorelasi dengan PM2.5 dan PM10")
st.markdown("---")
