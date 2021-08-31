from django.contrib import admin
from .models import *
 
# Register your models here.
class categorias(admin.ModelAdmin):
    list_display=(
        'id',
        'nombre'
    )

class preguntas(admin.ModelAdmin):
    list_display=(
        'id',
        'question',
    )

admin.site.register(QuesModel, preguntas)
admin.site.register(category, categorias)