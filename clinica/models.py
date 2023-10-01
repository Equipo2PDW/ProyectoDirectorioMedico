from django.db import models

class Especialidad(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo
    
    class Meta:
        verbose_name_plural="Especialidades"
        ordering=['tipo']

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural="Comunas"
        ordering=['nombre']

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre + " | comuna: " + self.comuna.nombre 
    class Meta:
        verbose_name_plural="Sucursales"
        ordering=['nombre']


class Medico(models.Model): #antecedentes y credenciales
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidades = models.ManyToManyField(Especialidad)
    sucursales = models.ManyToManyField(Sucursal)
    anos_experiencia = models.IntegerField() #antecedentes


    def __str__(self):
        return self.nombre + " " + self.apellido + " " + str (self.id)
    
    class Meta:
        verbose_name_plural="Médicos"
        ordering=['nombre']

class Estudios(models.Model): #credenciales
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    nombre_programaestudio = models.CharField(max_length=1000) #posgrado de cardiologia venas, etc
    nombre_casaestudios = models.CharField(max_length=200) #universidad, etc

    def __str__(self):
        return "Médico: "+ self.medico.apellido + " | " + self.nombre_programaestudio 
    class Meta:
        verbose_name_plural="Estudios"
        ordering=['medico']


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.apellido
    class Meta:
        verbose_name_plural="Pacientes"
        ordering=['nombre']


class citaMedica(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    centro = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    #motivo = models.CharField(max_length=200)
    #estado = models.CharField(max_length=200)

    def __str__(self):
        return "Médico: " + self.medico.apellido + " | Paciente: " + self.paciente.apellido + " | Fecha: " + str(self.fecha) + " | Hora: " + str(self.hora) 
    class Meta:
        verbose_name_plural="Citas Médicas"
        ordering=['medico']