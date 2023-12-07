from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=50, default="")
    father_name = models.CharField(max_length=50, default="")
    address = models.TextField(default="")

    def __str__(self):
        return f"{self.roll} - {self.name}"