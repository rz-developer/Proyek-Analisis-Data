import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memasukkan data tabel
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

avg_workday = day_df.groupby('workingday')['cnt'].mean()
# Mendefinisikan variabel avg_weekday yang diambil dari rata-rata jumlah pada kolom weekday
avg_weekday = day_df.groupby('weekday')['cnt'].mean()

# Memberi label pada chart workday dengan nilai Hari Kerja dan Hari Libur
label_workday = ['Hari Kerja', 'Hari Libur']
# Memberi label pada chart weekday dengan nilai hari dari senin sampai minggu
label_weekday = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']

# Mendefinisikan tampilan menggunakan Streamlit
st.title('Rata-rata Penyewaan Sepeda')
st.header('Hari Kerja vs Hari Libur')
st.write('Rata-rata Penyewaan Sepeda pada Hari Kerja:')
st.write(avg_workday)
st.write('Rata-rata Penyewaan Sepeda pada Hari Libur:')
st.write(avg_workday[::-1])  # Membalik urutan agar 'Hari Libur' terlebih dahulu

st.header('Hari dalam Seminggu')
st.write('Rata-rata Penyewaan Sepeda pada Setiap Hari:')
st.write(avg_weekday)

# Plot
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Pie chart untuk rata-rata pada hari kerja
axes[0].pie(avg_workday, labels=label_workday, autopct='%1.1f%%', colors=('#265073', '#9AD0C2'))
axes[0].set_title('Rata-rata Penyewaan Sepeda pada Hari Kerja')

# Pie chart untuk rata-rata pada setiap hari
axes[1].pie(avg_weekday, labels=label_weekday, autopct='%1.1f%%', colors=('#2D9596', 'lightgrey', '#9AD0C2', '#265073'))
axes[1].set_title('Rata-rata Penyewaan Sepeda pada Hari dalam Seminggu')

# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

weathersit_labels = {
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan'
}
# Menggunakan metode .map() untuk menambahkan kolom 'weathersit_label' ke DataFrame
day_df['weathersit_label'] = day_df['weathersit'].map(weathersit_labels)
# Mendefinisikan rata-rata jumlah pengguna sepeda berdasarkan cuaca
avg_weather = day_df.groupby('weathersit_label')['cnt'].mean().reset_index()

# Mendefinisikan tampilan menggunakan Streamlit
st.title('Rata-rata Jumlah Pengguna Sepeda Berdasarkan Kondisi Cuaca')
st.write('Rata-rata Jumlah Pengguna Sepeda untuk Setiap Kondisi Cuaca:')
st.write(avg_weather)

# Plot
plt.figure(figsize=(10,7))
# Ambil nilai x dan y dari weathersit_label dan cnt diikuti pewarnaan bar pada chart
plt.bar(avg_weather['weathersit_label'], avg_weather['cnt'], color="#2D9596")
# Menambahkan judul
plt.title('Rata-rata Jumlah Pengguna Sepeda Berdasarkan Kondisi Cuaca')
# Menambahkan keterangan pada garis x
plt.xlabel('Kondisi Cuaca')
# Menambahkan keterangan pada garis y
plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')
# Memutar label sumbu x sebesar 45 derajat
plt.xticks(rotation=45)
# Menambahkan grid pada sumbu y
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Menampilkan plot menggunakan Streamlit
st.pyplot(plt)

#Melakukan pendefinisian label 
#dengan membuat kamus pada kolom season dan mengisinya sesuai musim
season_labels = {
    1: "Dingin",
    2: "Semi",
    3: "Panas",
    4: "Gugur"
}
#Memasukkan label yang telah dibuat pada kolom season dengan fungsi .map
day_df['season_label'] = day_df['season'].map(season_labels)
# Mendefinisikan variabel avg_season untuk menghitung rata-rata jumlah pengguna sepeda sesuai season atau musim
avg_season = day_df.groupby('season_label')['cnt'].mean().reset_index()

# Mendefinisikan tampilan menggunakan Streamlit
st.title('Rata-rata Pengguna Sepeda pada 4 Musim')
st.write('Rata-rata Pengguna Sepeda untuk Setiap Musim:')
st.write(avg_season)

# Plot
plt.figure(figsize=(10,7))
# Ambil nilai x dan y dari season_label dan cnt diikuti pewarnaan bar pada chart
plt.bar(avg_season['season_label'], avg_season['cnt'], color="#2D9596")
# Judul
plt.title('Rata-rata Pengguna Sepeda pada 4 Musim')
# Menambahkan keterangan pada garis x
plt.xlabel('Musim')
# Menambahkan keterangan pada garis y
plt.ylabel('Rata-rata Pengguna Sepeda')
# Memutar label sumbu x sebesar 45 derajat
plt.xticks(rotation=45)
# Menambahkan grid pada sumbu y
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Menampilkan plot menggunakan Streamlit
st.pyplot(plt)

# Mendefinisikan variabel count_bikesharing, yakni jumlah dari kolom registered dan casual
count_bikesharing = [day_df['registered'].sum(), day_df['casual'].sum()]
# Mendefinisikan label
labels = ['Terdaftar', 'Tidak Terdaftar']

# Mendefinisikan tampilan menggunakan Streamlit
st.title('Jumlah Sewa Sepeda yang Terdaftar atau Tidak Terdaftar')
st.write('Jumlah Sewa Sepeda yang Terdaftar:', count_bikesharing[0])
st.write('Jumlah Sewa Sepeda yang Tidak Terdaftar:', count_bikesharing[1])

# Plot
plt.figure(figsize=(8, 6))
# Memanggil variabel count_bikesharing, label untuk membuat bar chart
plt.barh(labels, count_bikesharing, color=['#2D9596', '#9AD0C2'])
# Judul
plt.title('Jumlah Sewa Sepeda yang Terdaftar atau Tidak Terdaftar')
# Keterangan pada garis x
plt.xlabel('Jumlah Sewa')
# Keterangan pada garis y
plt.ylabel('Status')
# Menampilkan chart menggunakan Streamlit
st.pyplot(plt)