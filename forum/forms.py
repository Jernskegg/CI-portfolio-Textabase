from .models import comment
from django import forms


class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('comment_content',)
