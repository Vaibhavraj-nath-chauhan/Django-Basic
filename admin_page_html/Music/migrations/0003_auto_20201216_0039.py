# Generated by Django 3.1.4 on 2020-12-15 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0002_auto_20201216_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='mp3',
            field=models.FileField(max_length=400, upload_to='songs'),
        ),
    ]
