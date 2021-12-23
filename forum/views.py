from django.shortcuts import render
from django.views import generic
from .models import thread, comment
# Create your views here.

class threadList(generic.ListView):
    model = thread
    queryset = thread.objects.order_by('-posted_on')
    template_name = 'threads.html'
    paginate_by = 6
