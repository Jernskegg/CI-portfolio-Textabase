# Generated by Django 3.2.5 on 2021-12-27 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_alter_thread_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_upvote',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='upvote',
        ),
    ]