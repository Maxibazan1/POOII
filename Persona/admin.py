from django.contrib import admin
from .models import Persona


# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    
    list_display=('apellido','nombre','dni','id','email','vive','created','updated')
    list_filter=('vive','created')

admin.site.register(Persona,PersonaAdmin)
