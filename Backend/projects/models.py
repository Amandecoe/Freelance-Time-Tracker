from django.db import models

# Create your models here.

class Project(models.Model):
    id = models.DecimalField(primary_key=True)
    name = models.CharField(max_length=15)
    client_name = models.CharField(max_length=15)
    description = models.TextField()
    hourly_rate = models.DecimalField(decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

