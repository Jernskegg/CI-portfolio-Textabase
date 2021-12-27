from .models import comment, thread
from django import forms


class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('comment_content',)


class newThreadForm(forms.ModelForm):
    class Meta:
        model = thread
        exclude = [
            'slug',
            'thread_starter',
            'date_posted',
            'upvote',
        ]
