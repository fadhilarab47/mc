import requests
from pyrogram import Client, filters
from YukkiMusic import app

# Fungsi untuk mengambil data dari web
def fetch_data_from_web():
    url = "https://check-your-khodam.vercel.app/"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text  # Atau data yang Anda butuhkan dari respons
    else:
        return "Gagal mengakses data dari web."

# Handler untuk perintah /check
@app.on_message(filters.command("kodam"))
def check_data(client, message):
    result = fetch_data_from_web()
    message.reply_text(result)
