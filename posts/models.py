from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    category = models.CharField(max_length = 255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args = [str(self.id)])

class Category(models.Model):
    name = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
        

