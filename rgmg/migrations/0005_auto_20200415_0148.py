# Generated by Django 3.0.3 on 2020-04-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgmg', '0004_auto_20200409_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabla',
            name='columnaA',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='columnaB',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='columnaC',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='columnaD',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='columnaE',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='columnaF',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='tiempo',
            field=models.FloatField(default=0, null=True),
        ),
    ]
