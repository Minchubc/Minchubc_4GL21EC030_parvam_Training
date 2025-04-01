from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    usn = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=50)
    sem = models.IntegerField()
    course = models.CharField(max_length=50)

    def _str_(self):
        return self.name