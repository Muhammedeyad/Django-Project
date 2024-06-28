from django.db import models
from django.utils.text import slugify
import logging
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
    def saves(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)






