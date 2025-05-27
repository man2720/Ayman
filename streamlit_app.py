import streamlit as st

st.title("--selamat datang--")
st.write("Ini adalah website yang di buat untuk melengkapi tugas infomatika Ayman Zaber Oemar.")
st.write("mbe")
st.image("IMG-20250505-WA0000.jpg",width=200)
st.write("kurban tentar lagi euyy")
st.write("eid Mubarak")

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah bilangan Ganjil")


