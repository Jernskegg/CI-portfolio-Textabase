from . import views
from django.urls import path

urlpatterns = [
    path('', views.threadList.as_view(), name='home'),
    path('<slug:slug>/', views.threadPage.as_view(), name='threads_page'),
    path('addThread', views.addThread, name='addThread'),
    path('edit_thread/<thread_view_id>/', views.editThread,
         name='edit_thread'),
    path('delete_thread/<thread_view_id>/', views.deleteThread,
         name='delete_thread'),
]
