from django.db import models

# Create your models here.

class Autor (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    nascimento = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Libros (models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ManyToManyField(Autor, blank=True)


    def __str__(self):
        return self.title

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    libros = models.ForeignKey(Libros, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class CodigoDeBarra(models.Model):
    codigo = models.CharField(max_length=100)
    libro = models.OneToOneField(Libros, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo

class Usuario(models.Model):
    nmbre = models.CharField(max_length=100)
    libros = models.CharField(max_length=100)


    def __str__(self):
        return self.nmbre