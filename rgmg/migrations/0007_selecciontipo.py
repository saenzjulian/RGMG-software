# Generated by Django 3.0.3 on 2020-05-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgmg', '0006_auto_20200415_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeleccionTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letraVector', models.CharField(max_length=100)),
                ('tipoVector', models.CharField(max_length=100)),
            ],
        ),
    ]
