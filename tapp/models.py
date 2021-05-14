from django.db import models
import datetime

class TodoModel(models.Model):

    title = models.CharField(max_length=30)
    body = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def get_date(self, *args, **kwargs):
        date = self.date.today().weekday()
        date_format = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thur', 4:'Fri', 5:'Sat', 6:'Sun'}
        return date_format[date]

    def __str__(self):
        return self.title