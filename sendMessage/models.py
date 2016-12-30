from django.contrib.auth.models import Permission, User
from django.db import models


class Userdata(models.Model):
    mobile = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class UserHash(models.Model):
    user = models.ForeignKey(Userdata, on_delete=models.CASCADE)
    hashValue = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.name + ' ' + self.hashValue
