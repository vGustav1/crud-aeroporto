from django.contrib import admin
from .models import Airplane

class AirplaneAdmin(admin.ModelAdmin):
    list_display = ("matricula", "numero_Voo", "modelo", "procedencia", "destino", "numero_passageiros")


admin.site.register(Airplane,AirplaneAdmin)