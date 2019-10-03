# Generated by Django 2.0.13 on 2019-09-06 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vysledky_s', '0010_rozpis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rozpis',
            name='doma_venku',
        ),
        migrations.RemoveField(
            model_name='rozpis',
            name='hriste',
        ),
        migrations.RemoveField(
            model_name='rozpis',
            name='kolo',
        ),
        migrations.RemoveField(
            model_name='rozpis',
            name='souper',
        ),
        migrations.AddField(
            model_name='rozpis',
            name='domaci',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rozpis',
            name='hoste',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rozpis',
            name='datum',
            field=models.DateField(),
        ),
    ]
