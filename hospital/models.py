from django.db import models

# Create your models here.
from django.db import models
class Task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
# Create your models here.