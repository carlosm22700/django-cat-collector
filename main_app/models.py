from django.db import models

# Create your models here.
#this is the blueprint as to how data is structure
#lets us perform CRUD operations

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
