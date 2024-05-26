from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=25,blank=False)
    model=models.IntegerField()
    ram=models.CharField(max_length=25,blank=False)
    price=models.CharField(max_length=25,blank=False)

    def __str__(self):
        return self.name