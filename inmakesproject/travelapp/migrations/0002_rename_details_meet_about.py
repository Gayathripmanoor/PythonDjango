# Generated by Django 3.2.4 on 2021-06-24 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meet',
            old_name='details',
            new_name='about',
        ),
    ]
