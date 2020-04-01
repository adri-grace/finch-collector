from django.db import models
from django.urls import reverse


SEX = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('H', 'Hatchling')
)
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

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Nest(models.Model):
    clutch = models.CharField(max_length=20)
    broods = models.CharField(max_length=20)
    incubation = models.CharField(max_length=20)
    def __str__(self):
        return self.clutch
    def get_absolute_url(self):
        return reverse('nests_index')

class Siting(models.Model):
    date =models.DateField('siting date')
    sex = models.CharField(
        max_length=1,
        choices=SEX,
        default=SEX[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.sex} on {self.date}"
    class Meta:
        ordering = ['-date']