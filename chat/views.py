from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
import json
# Create your views here.
def chatbox(request):
    return render(request, 'praveen/chatbox.html')

def get_messages(request):
    messages = Message.objects.order_by('-timestamp')[:50]
    return JsonResponse({'messages': list(messages.values())})

def send_message(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        text = request.POST.get('text')
        Message.objects.create(username=username, text=text)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})