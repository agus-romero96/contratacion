from django.db import models

class Empleado(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cargo = models.ForeignKey('CargoSueldo', on_delete=models.RESTRICT, related_name='empleados')
    departamento = models.ForeignKey('Departamento', on_delete=models.RESTRICT, related_name='empleados')
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido


class CargoSueldo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=50)
    sueldo = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return self.nombre_cargo


class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.RESTRICT, related_name='contratos')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    tipo_contrato = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Contrato de {self.empleado.nombre} {self.empleado.apellido}"


class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)  # Aquí almacenamos la ciudad/ubicación
    
    def __str__(self):
        return self.nombre_departamento