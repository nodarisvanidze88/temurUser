from rest_framework import serializers
from .models import TemurUsers, Courses

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class TemurUsersSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    class Meta:
        model = TemurUsers
        fields = '__all__'
    def get_course(self, obj):
        return obj.course.course