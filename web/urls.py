from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('project/', views.project, name='web-project'),
    path('me/', views.me, name='web-me'),
    path('kontakt/', views.kontakt, name='web-kontakt'),
]