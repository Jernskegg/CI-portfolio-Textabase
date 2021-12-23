from . import views
from django.urls import path

urlpatterns = [
    path('', views.threadList.as_view(), name='home')
]