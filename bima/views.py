from django.shortcuts import render
# views.py

from django.http import JsonResponse

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import send_whatsapp_message
from googletrans import Translator

from pytube import YouTube

def download(request):
    if request.method == 'POST':
        youtube_link = request.POST.get('youtube_link')
        if youtube_link:
            try:
                yt = YouTube(youtube_link)
                context = {
                    'title': yt.title,
                    'streams': yt.streams.filter(only_audio=True),
                }
            except Exception as e:
                context = {
                    'error_message': 'Error: ' + str(e),
                }
        else:
            context = {
                'error_message': 'Please enter a YouTube link.',
            }
    else:
        context = {}
    return render(request, 'download.html', context)

# Create your views here.
# bima/views.py

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'POST':
        # Mendapatkan isi pesan WhatsApp dari request
        body = request.POST.get('Body', '').strip()
        from_whatsapp_number = request.POST.get('From', '').strip()
        to_whatsapp_number = request.POST.get('To', '').strip()

        # Mengirim pesan WhatsApp berupa judul video YouTube
        send_whatsapp_message(body, from_whatsapp_number, to_whatsapp_number)

    return HttpResponse()


# chatbot/views.py

# chatbot/views.py


def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        if user_input:
            user_input = user_input.lower().strip()
            response = handle_user_input(user_input)
        else:
            response = "Pybot tidak menerima input kosong."

        return JsonResponse({'response': response}, charset='utf-8')

    return render(request, 'chatbot.html')

def handle_user_input(user_input):
    if user_input.startswith('download '):
        # Panggil fungsi untuk mendownload video Instagram
        video_url = user_input.replace('download ', '').strip()
        # download_instagram_video(video_url)
        return f'Berhasil mendownload video dari {video_url}'

    elif user_input.startswith('translate '):
        # Panggil fungsi untuk menerjemahkan teks
        params = user_input.replace('translate ', '').strip().split(' ')
        if len(params) >= 2:
            text_to_translate = ' '.join(params[1:])
            target_language = params[0]

            # Translate the text using googletrans
            translator = Translator()
            translated_text = translator.translate(text_to_translate, dest=target_language)
            return f'Translate "{text_to_translate}" ke bahasa {target_language}: {translated_text.text}'

    # Default response for other input
    return 'Pybot tidak mengerti pesan Anda. Silakan coba lagi.'