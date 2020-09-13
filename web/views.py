from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import MailSender


# TODO: add database context

def home(request):
    return render(request, 'web/home.html', {'title': 'Home'})

def project(request):
    return render(request, 'web/project.html', {'title': 'Project'})

def me(request):
    return render(request, 'web/me.html', {'title': 'me'})

def kontakt(request):
    if request.method == 'GET':
        form = MailSender()
    else:
        form = MailSender(request.POST)
        if form.is_valid():
            form.save()
            """send_mail(
                'Subject here',
                'Here is the message.',
                'mkronborg6@gmail.com',
                ['mkronborg7@gmail.com'],
                fail_silently=False,
            )"""
            messages.success(request, f'Din besked er blevet sendt')
            return redirect('web-home')


    return render(request, "web/kontakt.html", {'form': form})
