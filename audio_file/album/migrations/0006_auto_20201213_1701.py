# Generated by Django 3.1.4 on 2020-12-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_auto_20201213_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albumdata',
            old_name='ststus',
            new_name='status',
        ),
        migrations.AddField(
            model_name='songs_list',
            name='audio',
            field=models.FileField(null=True, upload_to='audio'),
        ),
        migrations.AddField(
            model_name='songs_list',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='songs_list',
            name='artist',
            field=models.CharField(default='Unknown', max_length=30),
        ),
    ]
