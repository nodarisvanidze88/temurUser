from django.shortcuts import render
from .models import TemurUsers, Courses
from .serializers import TemurUsersSerializer, CoursesSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
import datetime
# Create your views here.

class TemurUserViews(ModelViewSet):
    queryset = TemurUsers.objects.all()
    serializer_class = TemurUsersSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data
        course_name = data.get('course')
        
        try:
            course_full = Courses.objects.get(course=course_name)
        except Courses.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = TemurUsers.objects.create(
                name=data.get("name"),
                tel=data.get("tel"),
                email=data.get("email"),
                registration=datetime.datetime.now(),
                course=course_full
            )
            user.save()
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class CourseViews(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer