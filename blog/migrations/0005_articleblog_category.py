# Generated by Django 5.0.3 on 2024-04-09 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleblog',
            name='category',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]