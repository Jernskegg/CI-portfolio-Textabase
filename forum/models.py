from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class thread(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    categories_choices = [
        ('GAM', 'Games'),
        ('BUG', 'Bugs'),
        ('BAN', 'Banter'),
        ('GEN', 'General')
    ]
    catergories = models.CharField(
        max_length=3,
        choices=categories_choices,
        default='GEN'
    )

    thread_starter = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name='thread_post')
    date_posted = models.DateTimeField(auto_now=True, editable=False)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    upvote = models.ManyToManyField(User, related_name="thread_upvotes",
                                    blank=True, default=False)

    def __str__(self):
        return self.title

    def upvoted(self):
        return self.upvote.count()


class comment(models.Model):
    comment_posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_atached_to = models.ForeignKey(thread, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True, editable=False)
    comment_content = models.TextField(max_length=255)
    comment_upvote = models.ManyToManyField(User,
                                            related_name="comment_upvotes",
                                            blank=True, default=False)
    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return str(self.comment_content) + str(self.comment_atached_to)

    def upvoted(self):
        return self.upvote.count()
