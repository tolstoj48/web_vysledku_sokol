# Generated by Django 2.0.9 on 2019-03-10 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vysledky_s', '0004_tabulka_sezona_tabulka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabulka',
            name='sezona_tabulka',
        ),
    ]
