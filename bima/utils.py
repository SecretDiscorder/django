# bima/utils.py

from twilio.rest import Client
from pytube import YouTube
from django.conf import settings

def send_whatsapp_message(body, from_whatsapp_number, to_whatsapp_number):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    # Memeriksa apakah pesan WhatsApp adalah tautan YouTube
    if body.startswith('https://www.youtube.com/') or body.startswith('https://youtu.be/'):
        try:
            # Mendapatkan informasi dari tautan YouTube menggunakan Pytube
            youtube_video = YouTube(body)
            video_title = youtube_video.title

            # Kirim pesan balasan ke nomor WhatsApp
            message = client.messages.create(
                body=f"Judul video YouTube: {video_title}",
                from_='whatsapp:' + from_whatsapp_number,
                to='whatsapp:' + to_whatsapp_number
            )

            return message.sid
        except Exception as e:
            # Jika terjadi kesalahan, kirimkan pesan balasan dengan informasi kesalahan
            message = client.messages.create(
                body="Terjadi kesalahan saat memproses tautan YouTube.",
                from_='whatsapp:' + from_whatsapp_number,
                to='whatsapp:' + to_whatsapp_number
            )

            return message.sid
    else:
        # Jika bukan tautan YouTube, kirimkan pesan balasan dengan informasi bahwa pesan tidak valid
        message = client.messages.create(
            body="Pesan tidak valid. Silakan kirimkan tautan YouTube.",
            from_='whatsapp:' + from_whatsapp_number,
            to='whatsapp:' + to_whatsapp_number
        )

        return message.sid
