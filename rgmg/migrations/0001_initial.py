# Generated by Django 3.0.3 on 2020-03-08 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contador', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TablaA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.IntegerField()),
                ('columnaA', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TablaB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.IntegerField()),
                ('columnaB', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TablaC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.IntegerField()),
                ('columnaC', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TablaD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.IntegerField()),
                ('columnaD', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TablaE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.IntegerField()),
                ('columnaE', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TablaF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.IntegerField()),
                ('columnaF', models.IntegerField()),
            ],
        ),
    ]