from django.test import TestCase

from django.contrib.auth.models import User
from .models import thread, comment

# Create your tests here.


class threadModelTest(TestCase):

    def test_set_upvotes_to_zero_when_created(self):
        user = User.objects.create(username="ADMIN2")
        item = thread.objects.create(title="something",
                                     thread_starter=user)
        self.assertEqual(item.times_upvoted(), 0)

    def test_set_upvotes_to_one_when_liked(self):
        user = User.objects.create(username="ADMIN2")
        item = thread.objects.create(title="something",
                                     thread_starter=user)
        some_list = [
            user,
        ]

        item.upvote.set(some_list)
        self.assertEqual(item.times_upvoted(), 1)


class commentModelTest(TestCase):

    def test_set_comment_upvotes_to_zero_when_created(self):
        user = User.objects.create(username="ADMIN2")
        thread_id = thread.objects.create(title="something",
                                          thread_starter=user)
        item = comment.objects.create(comment_posted_by=user,
                                      comment_atached_to=thread_id)
        self.assertEqual(item.times_upvoted(), 0)

    def test_set_comment_upvotes_to_one_when_liked(self):
        user = User.objects.create(username="ADMIN2")
        thread_id = thread.objects.create(title="something",
                                          thread_starter=user)
        item = comment.objects.create(comment_posted_by=user,
                                      comment_atached_to=thread_id)
        some_list = [
            user,
        ]

        item.comment_upvote.set(some_list)
        self.assertNotEqual(item.times_upvoted(), 0)
        self.assertEqual(item.times_upvoted(), 1)
