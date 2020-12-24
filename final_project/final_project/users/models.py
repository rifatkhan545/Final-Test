from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime


class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.TextField(max_length=500, null=True, blank=True)
    login_count = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return str(self.user)
