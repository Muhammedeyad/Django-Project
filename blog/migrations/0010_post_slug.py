# Generated by Django 2.0.13 on 2024-06-30 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='somewords', unique=True),
            preserve_default=False,
        ),
    ]
