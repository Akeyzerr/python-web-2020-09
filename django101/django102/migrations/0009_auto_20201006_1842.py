# Generated by Django 3.1.2 on 2020-10-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0008_auto_20201006_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='level_of_difficulty',
            field=models.CharField(choices=[('EA', 'Easy'), ('ME', 'Medium'), ('HA', 'Hard')], max_length=2),
        ),
    ]
