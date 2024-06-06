import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pymongo import MongoClient
from config import MONGO_DB_URI

from YukkiMusic import app

client = MongoClient(MONGO_DB_URI)
db = client.attendance_db

def get_today():
    return datetime.now().strftime("%Y-%m-%d")


@app.on_message(filters.command("absensi") & filters.group)
async def absensi(client, message):
    chat_id = message.chat.id
    today = get_today()
    
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Hadir", callback_data=f"hadir_{chat_id}_{today}")]]
    )
    
    await message.reply("Silakan klik tombol Hadir untuk mencatat kehadiran Anda:", reply_markup=keyboard)

@app.on_callback_query(filters.regex(r"^hadir_\d+_\d{4}-\d{2}-\d{2}$"))
async def hadir_callback(client, callback_query):
    data = callback_query.data.split("_")
    chat_id = int(data[1])
    today = data[2]
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    
    attendance_record = db.attendance.find_one({"chat_id": chat_id, "date": today, "user_id": user_id})
    
    if attendance_record:
        await callback_query.answer("Anda sudah tercatat hadir.", show_alert=True)
    else:
        db.attendance.insert_one({
            "chat_id": chat_id,
            "user_id": user_id,
            "user_name": user_name,
            "date": today
        })
        await callback_query.answer(f"Terima kasih {user_name}, Anda telah tercatat hadir.", show_alert=True)
        await client.send_message(chat_id, f"{user_name} telah hadir.")

@app.on_message(filters.command("rekap") & filters.group)
async def rekap(client, message):
    chat_id = message.chat.id
    today = get_today()
    
    attendance_records = db.attendance.find({"chat_id": chat_id, "date": today})
    hadir_list = [record["user_name"] for record in attendance_records]
    
    if hadir_list:
        hadir_names = "\n".join(hadir_list)
        await message.reply(f"Rekapitulasi kehadiran hari ini ({today}):\n{hadir_names}")
    else:
        await message.reply("Belum ada absensi yang dimulai hari ini. Gunakan perintah /absensi untuk memulai.")

@app.on_message(filters.command("rekap_harian") & filters.group)
async def rekap_harian(client, message):
    chat_id = message.chat.id
    
    attendance_records = db.attendance.find({"chat_id": chat_id}).sort("date")
    rekap_message = "Rekapitulasi harian:\n"
    current_date = ""
    
    for record in attendance_records:
        date = record["date"]
        user_name = record["user_name"]
        
        if date != current_date:
            current_date = date
            rekap_message += f"\nTanggal {date}:\n"
        rekap_message += f"- {user_name}\n"
    
    if rekap_message == "Rekapitulasi harian:\n":
        await message.reply("Belum ada data absensi. Gunakan perintah /absensi untuk memulai.")
    else:
        await message.reply(rekap_message)

@app.on_message(filters.command("clear") & filters.group)
async def clear(client, message):
    chat_id = message.chat.id
    
    db.attendance.delete_many({"chat_id": chat_id})
    await message.reply("Data absensi telah dihapus.")
