from django.db import models

# Create your models here.
class Announcements(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
