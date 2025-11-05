from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=15)
    client_name = models.CharField(max_length=15)
    description = models.TextField()
    hourly_rate = models.DecimalField(decimal_places=2)
