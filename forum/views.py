from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import thread
from .forms import commentForm, newThreadForm
from django.core.paginator import Paginator
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
        comments = thread_view.comments.order_by("-date_posted")
        paginate_comments = Paginator(comments, 5)
        page_number = request.GET.get('page')
        page_obj = paginate_comments.get_page(page_number)

        return render(
            request,
            "thread_page.html",
            {
                "thread_view": thread_view,
                "comments": page_obj,
                "commented": False,
                "comment_form": commentForm,
                'page_obj': page_obj,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = thread.objects
        thread_view = get_object_or_404(queryset, slug=slug)
        comments = thread_view.comments.order_by("-date_posted")

        comment_form = commentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.comment_posted_by = request.user
            comment.comment_atached_to = thread_view
            comment.save()

            return redirect('/'+slug+'/',)
        else:
            comment_form = comment_form

        return render(
            request,
            "thread_page.html",
            {
                "thread_view": thread_view,
                "comments": comments,
                "commented": True,
                "comment_form": commentForm,
            }
        )


def addThread(request):
    setform = newThreadForm
    if request.method == 'POST':
        form = setform(request.POST or None)
        if form.is_valid():
            newthread = form.save(commit=False)
            newthread.thread_starter = request.user
            newthread.save()
            return redirect('/'+newthread.slug+'/')
    else:
        form = newThreadForm
    context = {
        'form': form,
    }
    return render(request, 'new_thread.html', context)


def editThread(request, thread_view_id):
    edit_thread = get_object_or_404(thread, id=thread_view_id)
    form = newThreadForm(instance=edit_thread)
    setform = newThreadForm
    if request.method == 'POST':
        form = setform(request.POST, instance=edit_thread)
        if form.is_valid():
            newthread = form.save(commit=False)
            newthread.thread_starter = request.user
            newthread.save()
            return redirect('/'+newthread.slug+'/')
    context = {
        'form': form,
        'edit_thread': edit_thread,
    }
    return render(request, 'edit_thread.html', context)


def deleteThread(request, thread_view_id):
    delete_thread = get_object_or_404(thread, id=thread_view_id)
    delete_thread.delete()
    return redirect('home')
