# Generated by Django 4.2.7 on 2023-12-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_album_album_release_date_album_rating_between'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='rating_between',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
