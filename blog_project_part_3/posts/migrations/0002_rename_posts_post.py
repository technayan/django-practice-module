# Generated by Django 4.2.7 on 2023-12-07 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_rename_categories_category'),
        ('author', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
