from django.db import models
from projects.models import Project
from users.models import Freelancer
from datetime import timedelta
# Create your models here.
class Timelog(models.Model):
    id = models.DecimalField(primary_key=True, decimal_places=2, max_digits=10)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(null=True, blank=True)

    def save (self, *args, **kwargs):
        if self.start_time and self.end_time:
            self.duration = self.end_time - self.start_time
        super().save(*args, **kwargs)
    #saves the duration inside the database, no need for recalculation.
