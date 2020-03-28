from django.db import models

# Create your models here.
class Finch(models.Model):
    variety = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    nesting = models.CharField(max_length=100)
    behavior = models.CharField(max_length=100)
    conservation = models.CharField(max_length=100)

    def __str__(self):
        return self.variety