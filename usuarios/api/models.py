from django.db import models

class Usuario(models.Model):
    Nombre_Usuario = models.CharField(max_length=100, unique=True)
    apellido_usuario = models.CharField(max_length=100)
    correo = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.Nombre_Usuario} - {self.apellido_usuario} - {self.correo}'
