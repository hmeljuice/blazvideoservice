# Generated by Django 3.2.11 on 2022-02-03 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0007_alter_video_file_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file_location',
            field=models.FilePathField(path='upload_folder/'),
        ),
    ]
