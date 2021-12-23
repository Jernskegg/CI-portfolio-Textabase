from django.test import TestCase

from django.contrib.auth.models import User
from .models import thread

# Create your tests here.


class threadModelTest(TestCase):

    def test_set_upvotes_to_zero_when_created(self):
        user = User.objects.create(username="ADMIN2")
        item = thread.objects.create(title="something",
                                     thread_starter=user)
        self.assertEqual(item.upvote.count(), 0)
