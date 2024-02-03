from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
