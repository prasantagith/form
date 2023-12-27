from django.db import models

# Create your models here.
class Topics(models.Model):
    Tname=models.CharField(max_length=100,primary_key=True)
    
    def __str__(self):
        return self.Tname