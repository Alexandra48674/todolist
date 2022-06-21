from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    # on_delete=models.CASCADE -> when user is deleted - all tasks are deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    # auto_now_add=True -> auto added date and time
    created = models.DateTimeField(auto_now_add=True)

    # represents the class objects as a string
    def __str__(self):
        return self.title

    # checker
    class Meta:
        ordering = ['complete']
