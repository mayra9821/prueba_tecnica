# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Ecorregion(models.Model):
    idecorregion = models.AutoField(db_column='idEcorregion', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name="Ecorregion"
        verbose_name_plural="Ecorregiones"
        db_table = 'Ecorregiones'


class Proyectos(models.Model):
    idproyecto = models.AutoField(db_column='idProyecto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
        db_table = 'Proyectos'


class RegistroBioEspecies(models.Model):
    CHOICES=[
        ('Observacion Humana','Observacion_humana'),
        ("Especimen","Especimen")
        ]
    
    
    identificador = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=45, blank=True, null=True)
    familia = models.CharField(max_length=45, blank=True, null=True)
    nombre_comun = models.CharField(max_length=45, blank=True, null=True)
    proyecto = models.ForeignKey(Proyectos, models.DO_NOTHING, db_column='proyecto', blank=True, null=True)
    base_registro = models.CharField(max_length=45, blank=True, null=True, choices=CHOICES)
    anio_identificacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.CharField(max_length=45, blank=True, null=True)
    municipio = models.CharField(max_length=45, blank=True, null=True)
    localidad = models.CharField(max_length=45, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    autor = models.CharField(max_length=45, blank=True, null=True)
    fecha_captura = models.DateField(blank=True, null=True)
    ecorregion = models.ForeignKey(Ecorregion, models.DO_NOTHING, db_column='ecorregion', blank=True, null=True)

    class Meta:
        verbose_name="Registro biologico especies"
        verbose_name_plural="Registro biologico especies"
        db_table = 'Registro biologico especies'
