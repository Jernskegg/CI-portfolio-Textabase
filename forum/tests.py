from django.test import TestCase

from django.contrib.auth.models import User
from .models import thread, comment

# Create your tests here.


class threadModelTest(TestCase):

    def test_set_upvotes_to_zero_when_created(self):
        user = User.objects.create(username="ADMIN2")
        item = thread.objects.create(title="something",
                                     thread_starter=user)
        self.assertEqual(item.upvote.count(), 0)


class commentModelTest(TestCase):

    def test_set_commet_upvotes_to_zero_when_created(self):
        user = User.objects.create(username="ADMIN2")
        thread_id = thread.objects.create(title="something",
                                          thread_starter=user)
        item = comment.objects.create(comment_posted_by=user,
                                      comment_atached_to=thread_id)
        self.assertEqual(item.comment_upvote.count(), 0)
