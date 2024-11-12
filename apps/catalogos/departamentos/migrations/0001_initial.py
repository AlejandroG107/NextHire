# Generated by Django 4.2 on 2024-11-09 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('ID_Departamento', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo', models.CharField(max_length=50, unique=True, verbose_name='Código')),
                ('Nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
        ),
    ]