# Generated by Django 3.1.2 on 2020-10-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0007_auto_20201006_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='level_of_difficulty',
            field=models.IntegerField(choices=[('Easy', 'EA'), ('Medium', 'ME'), ('Hard', 'HA')]),
        ),
    ]
