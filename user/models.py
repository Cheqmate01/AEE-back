from django.db import models

# Create your models here.
# user/models.py
from django.db import models

class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100, blank=True, null=True)
    d_o_b = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    height = models.FloatField()
    weight = models.FloatField()
    jersey_size = models.CharField(max_length=10)
    shoe_size = models.CharField(max_length=10)
    passport_picture = models.ImageField(upload_to='passport_pictures/')
    full_picture = models.ImageField(upload_to='full_pictures/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"