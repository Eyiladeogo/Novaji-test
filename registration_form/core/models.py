from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, unique=True)
    mobile_network = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.phone_number}'
