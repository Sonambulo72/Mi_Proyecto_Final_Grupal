# Generated by Django 4.1.3 on 2022-11-09 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='prize',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
