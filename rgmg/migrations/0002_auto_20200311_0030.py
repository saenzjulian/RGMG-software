# Generated by Django 3.0.3 on 2020-03-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgmg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='contador',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablaa',
            name='columnaA',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablaa',
            name='tiempo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablab',
            name='columnaB',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablab',
            name='tiempo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablac',
            name='columnaC',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablac',
            name='tiempo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablad',
            name='columnaD',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablad',
            name='tiempo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablae',
            name='columnaE',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablae',
            name='tiempo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablaf',
            name='columnaF',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tablaf',
            name='tiempo',
            field=models.FloatField(),
        ),
    ]