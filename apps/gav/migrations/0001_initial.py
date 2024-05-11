# Generated by Django 5.0.4 on 2024-05-08 12:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('status', models.CharField(choices=[('F', 'FAMILIAR'), ('E', 'EGRESO'), ('J', 'JUBILADO'), ('C', 'CONTRATISTA'), ('M', 'MISC')], default='M', max_length=1, verbose_name='Tipo de visitante')),
                ('nac', models.CharField(blank=True, choices=[('VE', 'Venezolano'), ('EX', 'Extranjero')], max_length=2, null=True, verbose_name='Nacionalidad')),
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Cedula')),
                ('first_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Apellido')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, null=True, verbose_name='Género')),
            ],
            options={
                'ordering': ['dni'],
            },
        ),
        migrations.CreateModel(
            name='Avisitantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.DateField(verbose_name='Fecha del Dia')),
                ('hours', models.TimeField(verbose_name='Hora de Entrada')),
                ('hoursEx', models.TimeField(blank=True, null=True, verbose_name='Hora de Salida')),
                ('obs', models.TextField(blank=True, max_length=140, null=True, verbose_name='Observaciones')),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.cargo', verbose_name='Cargo')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.empleado', verbose_name='Cargo')),
                ('oficina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.oficina', verbose_name='Oficina a Visitar')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accesos_de_visitantes', to='gav.personas')),
            ],
            options={
                'verbose_name': 'Listado Accesos',
                'verbose_name_plural': 'Listado Accesos',
                'ordering': ['entry', 'hours'],
            },
        ),
    ]