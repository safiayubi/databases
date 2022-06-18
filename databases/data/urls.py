from django.urls import path
from . import views
from data import views
urlpatterns = [
   path('', views.home, name="home")
]