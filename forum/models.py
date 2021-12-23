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
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    upvote = models.ManyToManyField(User, related_name="thread_upvotes",
                                    blank=True, default=False)

    def __str__(self):
        return self.title

    def upvoted(self):
        return self.upvote.count()
