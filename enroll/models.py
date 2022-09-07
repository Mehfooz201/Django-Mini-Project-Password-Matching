from django.db import models

# Create your models here.

class Student(models.Model):
    stid = models.IntegerField()
    stname = models.CharField(max_length=50)
    stemail = models.EmailField(max_length=50)
    stpass= models.CharField(max_length=50)

    #Single Column with name Display
    # def __str__(self):
    #     return self.stname

    


