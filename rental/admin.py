from django.contrib import admin
from .models import Rental
# Register your models here.

class RentalAdmin(admin.ModelAdmin):
    list_display = ['who', 'what', 'when']
# 2- rejestrujemy klase
admin.site.register(Rental, RentalAdmin)