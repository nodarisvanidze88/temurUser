from django.db import models


class TemurUsers(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    class Meta:
        unique_together = ('name','tel','email')

    def __str__(self):
        return self.name