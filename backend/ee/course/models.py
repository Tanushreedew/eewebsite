from django.db import models

# Create your models here.


class Course(models.Model):
    program = models.CharField(max_length=50)
    semester = models.IntegerField(blank=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    credit = models.FloatField(blank=True)
    ltp = models.CharField(max_length=10)

    def __str__(self):
        return self.code


class CourseNew(models.Model):
    program = models.CharField(max_length=50)
    elective = models.BooleanField(default=False)
    semester = models.IntegerField(blank=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    credit = models.FloatField(blank=True)
    ltp = models.CharField(max_length=10)

    def __str__(self):
        return self.code


class Elective(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=60)
    credit = models.FloatField(blank=True)
    ltp = models.CharField(max_length=10)

    def __str__(self):
        return self.code
