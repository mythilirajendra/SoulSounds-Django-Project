# Generated by Django 2.1.7 on 2019-05-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_song_is_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]
