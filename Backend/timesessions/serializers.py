from rest_framework import serializers
from .models import Timelog

class TimelogSerializer(serializers.ModelSerializer):
    class Meta:
      model = Timelog
      fields = "__all__"
