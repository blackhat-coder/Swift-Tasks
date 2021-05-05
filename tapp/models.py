from django.db import models

class TodoModel(models.Model):

    title = models.CharField(max_length=30)
    body = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title