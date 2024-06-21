from YukkiMusic import app

from pyrogram import Client, filters
import random

# List khodams
khodams = [
    {"name": "Harimau Putih", "meaning": "Kamu kuat dan berani seperti harimau, karena pendahulumu mewariskan kekuatan besar padamu."},
    {"name": "Monyet Kekar", "meaning": "Kamu lincah dan cerdas, mampu menghadapi berbagai tantangan dengan ketangkasan."},
    {"name": "Naga Merah", "meaning": "Kamu memiliki kekuatan luar biasa dan kebijaksanaan, seperti naga yang legendaris."},
    {"name": "Burung Garuda", "meaning": "Kamu bebas dan perkasa, melambangkan kebebasan dan kemuliaan."},
    {"name": "Serigala Hitam", "meaning": "Kamu setia dan memiliki insting tajam, mampu melindungi diri dan orang lain."},
    {"name": "Macan Kumbang", "meaning": "Kamu misterius dan kuat, seperti macan yang jarang terlihat tapi selalu waspada."},
    {"name": "Kuda Emas", "meaning": "Kamu berharga dan kuat, siap untuk berlari menuju kesuksesan."},
    {"name": "Elang Biru", "meaning": "Kamu memiliki visi yang tajam dan dapat melihat peluang dari jauh."},
    {"name": "Harimau Loreng", "meaning": "Kamu tangguh dan memiliki kekuatan untuk melindungi dan menyerang."},
    {"name": "Gajah Putih", "meaning": "Kamu bijaksana dan memiliki kekuatan besar, lambang dari keberanian dan keteguhan hati."},
    {"name": "Banteng Sakti", "meaning": "Kamu kuat dan penuh semangat, tidak takut menghadapi rintangan."},
    {"name": "Ular Raksasa", "meaning": "Kamu memiliki kebijaksanaan dan kekuatan tersembunyi, siap menyerang jika diperlukan."},
    {"name": "Ikan Dewa", "meaning": "Kamu tenang dan penuh kedamaian, membawa rezeki dan keberuntungan."},
    {"name": "Kucing Hitam", "meaning": "Kamu misterius dan penuh dengan rahasia, membawa keberuntungan bagi yang memahami."},
    {"name": "Rusa Emas", "meaning": "Kamu anggun dan berharga, selalu dihargai oleh orang-orang di sekitarmu."},
    {"name": "Singa Bermahkota", "meaning": "Kamu lahir sebagai pemimpin, memiliki kekuatan dan kebijaksanaan seorang raja."},
    {"name": "Kijang Perak", "meaning": "Kamu cepat dan cekatan, selalu waspada dan siap untuk melompat lebih jauh."},
    {"name": "Anjing Pelacak", "meaning": "Kamu setia dan penuh dedikasi, selalu menemukan jalan menuju tujuanmu."},
    {"name": "Ayam Kutub", "meaning": "Jangan lupa share ke yang agar mereka tahu sosok aseli yang ada di dalam diri kamu"},
    {"name": "Topeng Monyet", "meaning": "Jangan lupa share ke yang agar mereka tahu sosok aseli yang ada di dalam diri kamu."},
    {"name": "Anjing Nigga", "meaning": "Jangan lupa share ke yang agar mereka tahu sosok aseli yang ada di dalam diri kamu."},
    {"name": "Harimau sakti", "meaning": "Jangan lupa share ke yang agar mereka tahu sosok aseli yang ada di dalam diri kamu."}
    # Add more khodams if needed
]

# Inisialisasi client Pyrogram
app = Client("my_bot")

# Command handler untuk /khodam
@app.on_message(filters.command(["khodam"]))
def random_khodam(client, message):
    # Ambil argumen setelah /khodam sebagai nama_user
    nama_user = message.text.split(maxsplit=1)[1].strip() if len(message.text.split(maxsplit=1)) > 1 else None
    
    if not nama_user:
        message.reply_text("Silakan masukkan nama user setelah perintah /khodam.")
        return
    
    # Cari khodam berdasarkan nama user
    found_khodam = None
    for khodam in khodams:
        if khodam["name"].lower() == nama_user.lower():
            found_khodam = khodam
            break
    
    # Jika khodam ditemukan, kirim pesan dengan nama dan maknanya
    if found_khodam:
        response = f"<b>Nama Khodam:</b> {found_khodam['name']}\n\n{found_khodam['meaning']}"
    else:
        response = f"Khodam untuk nama user '{nama_user}' tidak ditemukan."
    
    # Kirim pesan balasan dalam format HTML
    message.reply_text(response, parse_mode="html")

# Jalankan bot
app.run()
