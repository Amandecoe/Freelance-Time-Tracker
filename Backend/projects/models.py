from django.db import models
from django.utils.text import slugify
# Create your models here.

class Project(models.Model):
    id = models.DecimalField(primary_key=True, unique=True)
    name = models.CharField(max_length=15)
    slug = models.SlugField(unique=True, blank=True, null=True)
    client_name = models.CharField(max_length=15)
    description = models.TextField()
    hourly_rate = models.DecimalField(decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):  #slugifies the name and then saves it in the db in a unique_slug table
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            if Project.objects.filter(slug = unique_slug).exists():
                unique_slug = f'{self.slug}-{counter}'
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs) 
