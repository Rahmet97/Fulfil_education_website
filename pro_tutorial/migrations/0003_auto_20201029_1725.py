# Generated by Django 2.2.5 on 2020-10-29 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_tutorial', '0002_auto_20201028_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['teacher_name'], 'verbose_name': "O'qituvchi", 'verbose_name_plural': "O'qituvchilar"},
        ),
    ]
