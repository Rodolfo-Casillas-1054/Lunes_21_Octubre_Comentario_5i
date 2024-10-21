from django.contrib import admin
from .models import Alumno, Frase
# Register your models here.

class ComentarioIntLine(admin.TabularInline):
    model=Frase
    extra=1

class AlumnoAdmin(admin.ModelAdmin):
    fields=["apaterno", "amaterno", "nombre", "fechadenacimiento", "fechadeingreso"]
    list_display=["apaterno", "amaterno", "nombre"]
    inlines=[ComentarioIntLine]

admin.site.register(Alumno,AlumnoAdmin)

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    fields=["comentario", "Alumno_fk"]
    list_display=["comentario"]
