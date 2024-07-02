from django.db import models
from django.utils.text import slugify
import logging
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug= models.SlugField(unique= True)
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Bikes(models.Model):
    content = models.TextField()

class MyModel(models.Model):
    name = models.CharField(max_length= 100, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)