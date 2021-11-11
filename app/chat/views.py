from django.shortcuts import render

from .forms import ChatMessageForm


def home(request):
    form = ChatMessageForm()
    context = {"form": form}
    return render(request, "chat/home.html", context)
