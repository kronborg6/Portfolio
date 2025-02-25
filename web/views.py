from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import ListView
from django.contrib import messages
from .forms import MailSender
from .models import Post

# TODO: Add email sender til kontakt

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'web/home.html', context)

def project(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'web/project.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'web/project.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class PythonList(ListView):
    model = Post
    template_name = 'web/ppython.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class CSharpList(ListView):
    model = Post
    template_name = 'web/pcshap.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

def me(request):
    return render(request, 'web/me.html', {'title': 'me'})

def kontakt(request):
    if request.method == 'GET':
        form = MailSender()
    else:
        form = MailSender(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Din besked er blevet Modtaget')
            return redirect('web-home')

    return render(request, "web/kontakt.html", {'form': form})


