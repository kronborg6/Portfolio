from .models import Mail, Post
from django import forms

class MailSender(forms.ModelForm):
    Email = forms.EmailField()

    class Meta:
        model = Mail
        fields = ['Fornavn', 'Efternavn', 'Email', 'message']
