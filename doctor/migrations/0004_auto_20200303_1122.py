# Generated by Django 3.0.2 on 2020-03-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20200303_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.FileField(default=' ', upload_to=''),
        ),
    ]
