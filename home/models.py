# models.py
from django.db import models
from django.contrib.auth.models import User

class LongText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default='')
    text = models.TextField()
    state = models.CharField(max_length=50, default='')  # New column for state
    id = models.BigAutoField(primary_key=True)
    dt = models.DateField()
    tm = models.TimeField()

    def __str__(self):
        return f'{self.username} - {self.text[:20]}'