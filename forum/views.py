from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import thread
# Create your views here.


class threadList(generic.ListView):
    model = thread
    queryset = thread.objects.order_by('-date_posted')
    template_name = 'threads.html'
    paginate_by = 6


class threadPage(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = thread.objects
        thread_view = get_object_or_404(queryset, slug=slug)
        comments = thread.comment.order_by('comment_posted')
        upvoted = False
        if thread.upvote.filter(id=self.request.user.id).exists():
            upvoted = True

        return render(
            request,
            "thread_page.html",
            {
                "thread_view": thread_view,
                "comments": comments,
                "upvoted": upvoted
            }
        )
