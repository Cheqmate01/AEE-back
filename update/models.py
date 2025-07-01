from django.db import models

# Create your models here.
class Update(models.Model):
    event_picture = models.ImageField(upload_to='event_pictures/', blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_theme = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.event_theme}"