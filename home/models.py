from django.db import models
from datetime import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=70)
    desc = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    website_link = models.URLField(max_length=200)
    git_link = models.URLField(max_length=200)
    create_time = models.DateTimeField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    percent = models.IntegerField()

    def __str__(self):
        return self.name