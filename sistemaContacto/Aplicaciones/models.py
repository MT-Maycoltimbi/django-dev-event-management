from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class qrPersonal(models.Model):
    codigo = models.PositiveSmallIntegerField(default=5)
    nombre = models.CharField(max_length=35)

    def __str__(self):
        return "{0}".format(self.nombre)


class Persona(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    apellidoP = models.CharField(max_length=35)
    apellidoM = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    qrpersonal = models.ForeignKey(
        qrPersonal, null=False, blank=False, on_delete=models.CASCADE)

    def nombreCompleto(self):
        n = "{0} {1}, {2}"
        return n.format(self.apellidoP, self.apellidoM, self.nombres)

    def __str__(self):
        return self.nombreCompleto()


class Telefono(models.Model):
    persona = models.ForeignKey(
        Persona, null=False, blank=False, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return "{0} ({1})".format(self.numero, self.persona)


class Email(models.Model):
    persona = models.ForeignKey(
        Persona, null=False, blank=False, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)

    def __str__(self):
        return "{0} ({1})".format(self.email, self.persona)

# usuario registrados


# class Usuario(models.Model):
    # nombres = models.CharField(max_length=35)
    # email = models.CharField(max_length=100)
    # user = models.models.ForeignKey(User, on_delete=models.CASCADE)
