from django.http import HttpResponse
from django.shortcuts import render

from .forms import ChatMessageForm


def home(request):
    form = ChatMessageForm()
    context = {"form": form}
    return render(request, "chat/home.html", context)


def bot_response(request):
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            response_message = form.data["message"]
            http_response = HttpResponse()
            http_response.write(response_message)
            return http_response
