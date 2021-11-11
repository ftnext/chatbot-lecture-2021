from django import forms


class ChatMessageForm(forms.Form):
    message = forms.CharField(required=True, max_length=100)
