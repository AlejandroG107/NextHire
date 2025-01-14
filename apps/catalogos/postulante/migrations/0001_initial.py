# Generated by Django 4.2 on 2024-11-09 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plaza', '0001_initial'),
        ('profesion', '0001_initial'),
        ('municipio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('ID_Postulante', models.AutoField(primary_key=True, serialize=False)),
                ('Cedula', models.CharField(max_length=24, unique=True, verbose_name='Cédula')),
                ('Nombre_Postulante', models.CharField(max_length=56, verbose_name='Nombre del Postulante')),
                ('Apellidos', models.CharField(max_length=56, verbose_name='Apellidos')),
                ('Sexo', models.CharField(max_length=17, verbose_name='Sexo')),
                ('Correo', models.CharField(max_length=100, verbose_name='Correo Electrónico')),
                ('Telefono', models.CharField(max_length=16, verbose_name='Teléfono')),
                ('Fecha_Nacimiento', models.CharField(max_length=24, verbose_name='Fecha Nacimiento')),
                ('Direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('Experiencia_Laboral', models.CharField(max_length=100, verbose_name='Experiencia Laboral')),
                ('ID_Municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='municipio.municipio', verbose_name='Municipio')),
                ('ID_Profesion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profesion.profesion', verbose_name='Profesión')),
            ],
            options={
                'verbose_name_plural': 'Postulantes',
            },
        ),
        migrations.CreateModel(
            name='DetallePostulante',
            fields=[
                ('ID_DETALLE_POSTULANTE', models.AutoField(primary_key=True, serialize=False)),
                ('Comentarios', models.CharField(max_length=200, verbose_name='Comentarios')),
                ('ID_DetallePlaza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plaza.detalleplaza', verbose_name='DetallePlaza')),
                ('ID_Postulante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles', to='postulante.postulante', verbose_name='Postulante')),
            ],
            options={
                'verbose_name_plural': 'Detalles de Postulante',
            },
        ),
    ]
