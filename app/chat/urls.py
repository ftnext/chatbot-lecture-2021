from django.urls import path

from chat import views

app_name = "chat"

urlpatterns = [
    path("", views.home, name="home"),
    path("bot-response/", views.bot_response, name="bot_response"),
]
