from django.db import models
from projects.models import Project
# Create your models here.
class Timelog(models.Model):
    id = models.DecimalField(primary_key=True)
    project_id = models.DecimalField()
    start_time = models.DateTimeField()
    duration = models.DurationField()
    project = models.Foreignkey(Project, on_delete = models.CASCADE)
