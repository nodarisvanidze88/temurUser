from django.db import models

class Courses(models.Model):
    course = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.course

class TemurUsers(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    registration = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('name','tel','email')

    def __str__(self):
        return self.name