# Generated by Django 2.0.9 on 2018-12-08 19:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vysledky_s', '0003_tabulka'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabulka',
            name='sezona_tabulka',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
