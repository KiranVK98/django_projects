# Generated by Django 3.1.2 on 2020-12-27 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0005_auto_20201227_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iso',
            old_name='name',
            new_name='iso',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='name',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='name',
            new_name='states',
        ),
    ]
