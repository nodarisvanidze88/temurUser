from rest_framework import serializers
from .models import TemurUsers

class TemurUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemurUsers
        fields = '__all__'