from django.contrib import admin
from .models import Libros, Autor, Biblioteca, CodigoDeBarra, Usuario

class LibrosAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'description',)

class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'nascimento', 'ativo',)

class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'telefono', 'libros',)

class CodigoDeBarraAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'libro',)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nmbre', 'libros',)

# Register your models here.
admin.site.register(Libros, LibrosAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Biblioteca, BibliotecaAdmin)
admin.site.register(CodigoDeBarra, CodigoDeBarraAdmin)
admin.site.register(Usuario, UsuarioAdmin)


