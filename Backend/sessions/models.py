from django.db import models

# Create your models here.
class Timelog(models.Model):
    id = models.DecimalField(primary_key=True)
    project_id = models.DecimalField()
    start_time = models.DateTimeField()
    duration = models.DurationField()
