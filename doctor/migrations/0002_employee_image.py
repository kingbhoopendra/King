# Generated by Django 3.0.2 on 2020-02-28 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.FileField(default=' ', upload_to=''),
        ),
    ]
