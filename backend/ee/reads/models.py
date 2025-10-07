from django.db import models

class Reads(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100) 
    def __str__(self) -> str:
        return self.author