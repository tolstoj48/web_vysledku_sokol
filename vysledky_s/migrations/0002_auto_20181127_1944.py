# Generated by Django 2.0.9 on 2018-11-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vysledky_s', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utkani',
            name='datum',
            field=models.CharField(max_length=100),
        ),
    ]