import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Demo Streamlit", layout="wide")

# Title
st.title("🚀 Aplikasi Streamlit Pertamaku di VS Code")
st.write("Selamat datang! Ini adalah contoh aplikasi Streamlit.")

# Sidebar
st.sidebar.header("⚙️ Pengaturan")
nama = st.sidebar.text_input("Nama kamu", "Pengguna")
jumlah_data = st.sidebar.slider("Jumlah data", 10, 100, 50)

# Main content
st.header(f"Halo, {nama}!")

# Generate data contoh
data = pd.DataFrame({
    'Index': range(jumlah_data),
    'Nilai': np.random.randn(jumlah_data).cumsum(),
    'Kategori': np.random.choice(['A', 'B', 'C'], jumlah_data)
})

# Tampilkan metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Data", len(data))
col2.metric("Rata-rata", f"{data['Nilai'].mean():.2f}")
col3.metric("Standar Deviasi", f"{data['Nilai'].std():.2f}")

# Tabel data
st.subheader("📊 Tampilan Data")
st.dataframe(data, use_container_width=True)

# Chart
st.subheader("📈 Visualisasi")
st.line_chart(data.set_index('Index')['Nilai'])

# Interaksi
st.subheader("🔍 Filter Data")
kategori = st.multiselect("Pilih Kategori", data['Kategori'].unique())
if kategori:
    filtered_data = data[data['Kategori'].isin(kategori)]
    st.write(f"Menampilkan {len(filtered_data)} data")
    st.dataframe(filtered_data)