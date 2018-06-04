from django.db import models


class ProjectSRC(models.Model):
    filename = models.CharField(unique=True, max_length=40)
    location = models.CharField(max_length=50)
    size = models.CharField(max_length=5)


class ProjectBinary(models.Model):
    filename = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    size = models.CharField(max_length=6)
