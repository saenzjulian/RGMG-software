# Generated by Django 3.0.3 on 2020-04-10 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgmg', '0003_auto_20200409_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabla',
            name='columnaA',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='columnaB',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='columnaC',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='columnaD',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='columnaE',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='columnaF',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='tiempo',
            field=models.FloatField(null=True),
        ),
    ]
