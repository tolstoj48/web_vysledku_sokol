# Generated by Django 2.0.9 on 2019-03-14 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vysledky_s', '0005_remove_tabulka_sezona_tabulka'),
    ]

    operations = [
        migrations.AddField(
            model_name='utkani',
            name='koment',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
