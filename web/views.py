from django.shortcuts import render

def home(request):

    return render(request, 'web/home.html', {'title': 'Home'})


def project(request):
    return render(request, 'web/project.html', {'title': 'Project'})

def me(request):
    return render(request, 'web/me.html', {'title': 'me'})

def kontakt(request):
    return render(request, 'web/kontakt.html', {'title': 'kontakt'})