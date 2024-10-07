from django.db import models

# Create your models here.
class Prospect(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    # published_date = models.DateField()
    # prospectid = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.name