# Generated by Django 2.2.5 on 2020-10-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='pupil_female',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pupil',
            name='pupil_male',
            field=models.BooleanField(default=False),
        ),
    ]