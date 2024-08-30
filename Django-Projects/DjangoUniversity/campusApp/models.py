from django.db import models

# Create your models here.
class UniversityCampus(models.Model): #created UniversityCampus Class with models.Model arguments
    Campus_Name=models.CharField(max_length=60, default="",blank=True,null=False) #here and below are the attributes for the University Campus class
    State=models.CharField(max_length=2, default="",blank=True,null=False)
    Campus_ID=models.IntegerField(max_length=20, default="",blank=True,null=False)

    objects = models.Manager() #this is the objects manager which is the interface between the model and the database

    def __str__(self): #displays university campus in the browser on the admin page
        return self.Campus_Name