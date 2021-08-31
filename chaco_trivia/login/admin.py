from django.contrib import admin
from .models import *
 
# Register your models here.
class categorias(admin.ModelAdmin):
    list_display=(
        'id',
        'nombre'
    )

admin.site.register(QuesModel)
admin.site.register(category, categorias)