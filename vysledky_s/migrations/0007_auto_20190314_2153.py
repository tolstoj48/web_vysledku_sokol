# Generated by Django 2.0.9 on 2019-03-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vysledky_s', '0006_utkani_koment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utkani',
            name='goly',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
