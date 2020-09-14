from django.urls import path
from .views import PostListView, PythonList, CSharpList
from . import views

# TODO: lave et degise og add info til de forskilge sider

urlpatterns = [
    path('', views.home, name='web-home'),
    path('project/', PostListView.as_view(), name='web-project'),
    path('project/python/', PythonList.as_view(), name='web-python'),
    path('project/csharp/', CSharpList.as_view(), name='web-c#'),
    path('me/', views.me, name='web-me'),
    path('kontakt/', views.kontakt, name='web-kontakt'),
]

