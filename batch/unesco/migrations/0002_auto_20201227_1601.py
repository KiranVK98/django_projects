# Generated by Django 3.1.2 on 2020-12-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='site',
            name='justification',
            field=models.TextField(),
        ),
    ]