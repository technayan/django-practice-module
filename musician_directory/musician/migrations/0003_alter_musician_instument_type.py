# Generated by Django 4.2.7 on 2023-12-08 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0002_alter_musician_instument_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='instument_type',
            field=models.CharField(choices=[('guiter', 'Guiter'), ('piano', 'Piano'), ('violin', 'Violin')], max_length=50),
        ),
    ]
