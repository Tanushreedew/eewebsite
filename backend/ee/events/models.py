from django.db import models

# Create your models here.


class Events(models.Model):
    title = models.TextField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.IntegerField()
    month = models.CharField(max_length=50)
    day = models.CharField(max_length=15)
    time = models.TimeField()
    link = models.URLField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.title
