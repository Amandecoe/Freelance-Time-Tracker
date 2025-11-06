from .models import Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        Fields = ["id","name", "slug", "client_name", "description", "hourly_rate","created_at", "updated_at" ]