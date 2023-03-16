from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200) 
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

