# Generated by Django 5.0.6 on 2024-07-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=500, upload_to='gallery'),
        ),
    ]