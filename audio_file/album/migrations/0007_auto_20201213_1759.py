# Generated by Django 3.1.4 on 2020-12-13 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0006_auto_20201213_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs_list',
            name='audio',
            field=models.FileField(max_length=200, null=True, upload_to='audio'),
        ),
    ]
