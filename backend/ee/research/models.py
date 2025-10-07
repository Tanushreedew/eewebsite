from django.db import models

# Create your models here.

class Research(models.Model):
    specialization = models.CharField(max_length=50)
    person = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    name = models.CharField(max_length=500)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.person


class PGLabs(models.Model):
    name = models.CharField(max_length=5000)
    description = models.CharField(max_length=10000)
    person = models.CharField(max_length=500)
    keywords = models.CharField(max_length=10000)
    review = models.JSONField(null=True)
    link = models.URLField()
    location = models.CharField(max_length=5000)
    area = models.CharField(max_length=5000)
    category = models.CharField(max_length=50)
    equipments = models.JSONField(null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.name
    
class UGLabs(models.Model):
    name = models.CharField(max_length=1000)
    experiments = models.JSONField(null=True)
    equipments = models.JSONField(null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.name


class Papers(models.Model):
    person = models.CharField(max_length=500)
    year = models.IntegerField()
    paper = models.CharField(max_length=500)

    def __str__(self):
        return self.person


class Projects(models.Model):
    title = models.CharField(max_length=500)
    worker = models.CharField(max_length=500)
    funding = models.CharField(max_length=500)
    duration = models.CharField(max_length=50)
    project_type = models.CharField(max_length=500)

    def __str__(self):
        return self.title
