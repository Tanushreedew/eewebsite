from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    # date = models.IntegerField()
    month = models.CharField(max_length=50)
    day = models.CharField(max_length=255)
    time = models.TimeField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
        
