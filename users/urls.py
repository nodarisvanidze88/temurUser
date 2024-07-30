from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TemurUserViews, CourseViews
router = DefaultRouter()
router.register(r'users',TemurUserViews, basename='users')
router.register(r'course', CourseViews, basename='course')
urlpatterns = [
    path('', include(router.urls))
]
