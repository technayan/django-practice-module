from django.db import models
from musician.models import Musician
import datetime

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date = models.DateField(default=datetime.date.today)
    RATING = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    rating_between = models.IntegerField(choices=RATING)

    def __str__(self):
        return f"{self.album_name} - {self.musician}"