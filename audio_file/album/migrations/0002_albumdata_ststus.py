# Generated by Django 3.1.4 on 2020-12-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumdata',
            name='ststus',
            field=models.BooleanField(default=True),
        ),
    ]
