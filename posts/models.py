from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='posts')
    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.title
