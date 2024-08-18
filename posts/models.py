from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title
