# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ciudades(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    nombre = models.CharField(blank=True, null=True, max_length=50)
    id_departamentos = models.ForeignKey('Departamentos', models.DO_NOTHING, db_column='id_departamentos', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ciudades'

class Clientes(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    apellido = models.CharField(max_length=50)
    ci = models.CharField(max_length=20)
    id_ciudades = models.ForeignKey('Ciudades', on_delete=models.CASCADE)
    estado = models.CharField(max_length=12)
    class Meta:
        managed = False
        db_table = 'Clientes'

class Departamentos(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    nombre = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'Departamentos'


class Habitaciones(models.Model):
    id_hoteles = models.ForeignKey('Hoteles', models.DO_NOTHING, db_column='id_hoteles', blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)  # This field type is a guess.
    numero = models.SmallIntegerField(blank=True, null=True)
    precio = models.TextField(blank=True, null=True)  # This field type is a guess.
    descripcion = models.CharField(blank=True, null=True, max_length=50)
    capacidad = models.TextField(blank=True, null=True)  # This field type is a guess.
    estado = models.CharField(blank=True, null=True, max_length=12)

    class Meta:
        managed = False
        db_table = 'Habitaciones'


class Hoteles(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    nombre = models.CharField(blank=True, null=True, max_length=50)
    direccion = models.CharField(blank=True, null=True, max_length=50)
    telefono = models.CharField(blank=True, null=True, max_length=50)
    correo = models.CharField(blank=True, null=True, max_length=50)
    id_ciudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='id_ciudad', blank=True, null=True)
    estado = models.CharField(blank=True, null=True, max_length=12)

    class Meta:
        managed = False
        db_table = 'Hoteles'


class Personales(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length=50)
    fecha_alta = models.DateField(blank=True, null=True)
    apellido = models.CharField(blank=True, null=True, max_length=50)
    ci = models.CharField(blank=True, null=True, max_length=20)
    telefono = models.CharField(blank=True, null=True, max_length=50)
    correo = models.CharField(blank=True, null=True, max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    id_ciudades = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='id_ciudades', blank=True, null=True)
    id_roles = models.ForeignKey('Roles', models.DO_NOTHING, db_column='id_roles', blank=True, null=True)
    estado = models.CharField(blank=True, null=True, max_length=12)

    class Meta:
        managed = False
        db_table = 'Personales'


class Reservas(models.Model):
    id_clientes = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='id_clientes', blank=True, null=True)
    id_habitaciones = models.ForeignKey(Habitaciones, models.DO_NOTHING, db_column='id_habitaciones', blank=True, null=True)
    fecha_entrada = models.DateField(blank=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)
    precio = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_personales = models.ForeignKey(Personales, models.DO_NOTHING, db_column='id_personales', blank=True, null=True)
    observacion = models.CharField(blank=True, null=True, max_length=50)
    estado = models.CharField(blank=True, null=True, max_length=12)

    class Meta:
        managed = False
        db_table = 'Reservas'


class Roles(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    nombre = models.CharField(blank=True, null=True, max_length=50)
    descripcion = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'Roles'


class Usuarios(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length=50)
    clave = models.CharField(blank=True, null=True, max_length=50)
    id_personales = models.ForeignKey(Personales, models.DO_NOTHING, db_column='id_personales', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuarios'
