# Generated by Django 3.2.5 on 2021-12-26 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20211226_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_atached_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='forum.thread'),
        ),
    ]