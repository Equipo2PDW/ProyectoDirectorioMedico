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

class Estudios(models.Model): #credenciales
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
    nombre_programaestudio = models.CharField(max_length=100) #posgrado de cardiologia venas, etc
    nombre_casaestudios = models.CharField(max_length=200) #universidad, etc

    def __str__(self):
        return self.medico + " " + self.nombre_programaestudio 
    class Meta:
        verbose_name_plural="Estudios"
        ordering=['medico']

class Medico(models.Model): #antecedentes y credenciales
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidades = models.ManyToManyField(Especialidad)
    ubicaciones = models.ManyToManyField(Comuna)
    anos_experiencia = models.IntegerField() #antecedentes


    def __str__(self):
        return self.nombre + " " + self.apellido
    
    class Meta:
        verbose_name_plural="Médicos"
        ordering=['nombre']