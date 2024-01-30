from django.db import models
from django.contrib.auth.models import AbstractUser



class UserMessengerModel(AbstractUser):
    MARRIED = 'married'
    SINGLE = 'single'
    COMPLICATED = 'complicated'
    DIVORCE = 'divorce'

    CHOICES = [
        (MARRIED, 'married'),
        (SINGLE, 'single'),
        (COMPLICATED, 'complicated'),
        (DIVORCE, 'divorce')
    ]
    phone = models.CharField(max_length=15)
    image = models.ImageField(verbose_name='images')
    profession=models.CharField(max_length=255)
    relationship=models.CharField(max_length=50, choices=CHOICES)

