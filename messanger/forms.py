import datetime

from django import forms
import pytz
from messanger.models import FeedbackUser


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label="Номер телефона",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )

    def save(self):
        name = self.cleaned_data['name']
        phone = self.cleaned_data['phone']
        message = self.cleaned_data['message']
        FeedbackUser.objects.create(name=name, phone_number=phone, message=message, timestamp=datetime.datetime.now())
