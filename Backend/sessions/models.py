from django.db import models
from projects.models import Project
from users.models import Freelancer
# Create your models here.
class Timelog(models.Model):
    id = models.DecimalField(primary_key=True)
    project = models.Foreignkey(Project, on_delete = models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(null=True, blank=True)
