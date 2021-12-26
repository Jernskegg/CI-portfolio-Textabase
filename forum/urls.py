from . import views
from django.urls import path

urlpatterns = [
    path('', views.threadList.as_view(), name='home'),
    path('<slug:slug>/', views.threadPage.as_view(), name='threads_page'),
]
