# Generated by Django 2.2.5 on 2020-10-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d/', verbose_name='Blog Rasmi:')),
                ('blog_url', models.URLField(max_length=300, verbose_name='Telegram Linki:')),
                ('blog_description', models.TextField(verbose_name='Blog Tarifi:')),
                ('blog_published', models.DateTimeField(auto_now_add=True)),
                ('blog_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Bloglar',
                'ordering': ['blog_published', 'blog_updated'],
            },
        ),
    ]
