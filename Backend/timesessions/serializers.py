from rest_framework import serializers
from .models import Timelog

class TimelogSerializer(serializers.ModelSerializer):
    class Meta:
      model = Timelog
      fields = {"id", "project", "freelancer", "notes", "start_time", "end_time", "duration"}
