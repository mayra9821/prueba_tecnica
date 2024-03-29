# Generated by Django 2.2 on 2021-07-16 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecorregion',
            fields=[
                ('idecorregion', models.AutoField(db_column='idEcorregion', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Ecorregion',
                'verbose_name_plural': 'Ecorregiones',
                'db_table': 'Ecorregiones',
            },
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('idproyecto', models.AutoField(db_column='idProyecto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'db_table': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='RegistroBioEspecies',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False)),
                ('especie', models.CharField(blank=True, max_length=45, null=True)),
                ('familia', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre_comun', models.CharField(blank=True, max_length=45, null=True)),
                ('base_registro', models.CharField(blank=True, choices=[('Observacion Humana', 'Observacion_humana'), ('Especimen', 'Especimen')], max_length=45, null=True)),
                ('anio_identificacion', models.TextField(blank=True, null=True)),
                ('departamento', models.CharField(blank=True, max_length=45, null=True)),
                ('municipio', models.CharField(blank=True, max_length=45, null=True)),
                ('localidad', models.CharField(blank=True, max_length=45, null=True)),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('autor', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha_captura', models.DateField(blank=True, null=True)),
                ('ecorregion', models.ForeignKey(blank=True, db_column='ecorregion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='registro.Ecorregion')),
                ('proyecto', models.ForeignKey(blank=True, db_column='proyecto', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='registro.Proyectos')),
            ],
            options={
                'verbose_name': 'Registro biologico especies',
                'verbose_name_plural': 'Registro biologico especies',
                'db_table': 'Registro biologico especies',
            },
        ),
    ]
