from django.shortcuts import render
from .models import TemurUsers
from .serializers import TemurUsersSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class TemurUserViews(ModelViewSet):
    queryset = TemurUsers.objects.all()
    serializer_class = TemurUsersSerializer