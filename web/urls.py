from django.urls import path
from . import views

# TODO: lave et degise og add info til de forskilge sider

urlpatterns = [
    path('', views.home, name='web-home'),
    path('project/', views.project, name='web-project'),
    path('me/', views.me, name='web-me'),
    path('kontakt/', views.kontakt, name='web-kontakt'),
]

