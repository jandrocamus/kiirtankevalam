# Generated by Django 2.1.1 on 2019-05-18 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Song', '0003_auto_20190518_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='isfavourite',
            old_name='is_favourite',
            new_name='is_favorite',
        ),
    ]