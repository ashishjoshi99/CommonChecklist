# Generated by Django 3.0.4 on 2020-03-31 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='boards',
            field=models.IntegerField(),
        ),
    ]
