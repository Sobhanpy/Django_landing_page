from django.urls import path, include
from .views import home

app_name = 'root'

urlpatterns = [
    path("", home, name="home"),
]