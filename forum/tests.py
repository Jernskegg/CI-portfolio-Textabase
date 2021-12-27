from django.test import TestCase
from .forms import newThreadForm

# Create your tests here.
# to test these I have added a database-debug mode inside settings


class testThreadsForm(TestCase):

    def test_title_cannot_be_empty(self):
        form = newThreadForm({'title': ''})
        self.assertFalse(form.is_valid())

    def test_thread_content_cannot_be_empty(self):
        form = newThreadForm({'content': ''})
        self.assertFalse(form.is_valid())

    def test_thread_author_must_be_assigned(self):
        form = newThreadForm({'testThreadsForm.thread_starter': ''})
        self.assertFalse(form.is_valid())
