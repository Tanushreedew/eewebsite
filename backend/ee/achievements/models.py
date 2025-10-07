from django.db import models

# Create your models here.
class Books(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=5000)
    author = models.CharField(max_length=5000, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    publication = models.CharField(max_length=5000, null=True)

    def __str__(self) -> str:
        return self.name


class StudentAwards(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=5000)
    award = models.CharField(max_length=5000, null=True)
    roll_no = models.IntegerField(null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self) -> str:
        return self.name

class FacultyAwards(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=5000)
    award = models.CharField(max_length=5000, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self) -> str:
        return self.award

class Patent(models.Model):
    year = models.CharField(max_length=50)
    name = models.CharField(max_length=5000)
    pi = models.CharField(max_length=5000, null=True)
    uuid = models.CharField(max_length=5000, null=True)
    status = models.CharField(max_length=5000, null=True)

    def __str__(self) -> str:
        return self.uuid