from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ChatMessageForm

chatbot = ChatBot(**settings.CHATTERBOT)


def home(request):
    form = ChatMessageForm()
    context = {"form": form}
    return render(request, "chat/home.html", context)


def bot_response(request):
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            input_message = form.data["message"]
            response_message = chatbot.get_response(input_message)
            http_response = HttpResponse()
            http_response.write(response_message)
            return http_response
