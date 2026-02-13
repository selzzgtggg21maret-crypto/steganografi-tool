TOOL STEGANOGRAFI BY Harry

Tool sederhana untuk menyisipkan dan membaca pesan rahasia dalam gambar PNG menggunakan metode LSB.

---

📱 Instalasi di Termux

1. Update package:

pkg update && pkg upgrade

2. Install Python:

pkg install python

3. Install dependency:

pkg install clang make libjpeg-turbo libpng freetype libwebp

4. Install library Python:

pip install --upgrade pip
pip install pillow

5. Izinkan akses storage:

termux-setup-storage

---

💻 Instalasi di Linux (Kali / Ubuntu / Debian)

1. Update system:

sudo apt update && sudo apt upgrade

2. Install Python & pip:

sudo apt install python3 python3-pip

3. Install dependency Pillow:

sudo apt install libjpeg-dev zlib1g-dev libpng-dev libfreetype6-dev libwebp-dev

4. Install library Python:

pip3 install pillow

---

▶ Cara Menjalankan Tool

Masuk ke folder project, lalu jalankan:

python stego.py

atau di Linux:

python3 stego.py

---

📌 Cara Menggunakan

Setelah dijalankan, pilih menu:

1. Encode
2. Decode

---

🔐 Encode (Menyisipkan Pesan)

- Pilih "1"
- Masukkan path gambar PNG

Contoh Termux:

/storage/emulated/0/Download/gambar.png

Contoh Linux:

/home/user/gambar.png

- Masukkan nama output gambar (PNG)
- Masukkan pesan rahasia

---

🔓 Decode (Membaca Pesan)

- Pilih "2"
- Masukkan path gambar yang sudah berisi pesan

---

⚠ Catatan Penting

- Gunakan format PNG (bukan JPG)
- Jangan upload ke platform yang mengkompres gambar
- Gunakan path lengkap agar tidak error
- Jangan overwrite file asli

---

🚀 Tips

- Gunakan gambar beresolusi besar untuk menyimpan pesan lebih panjang
- Test encode & decode sebelum dibagikan
- Simpan file hasil dalam format PNG tanpa kompresi ulang

---
