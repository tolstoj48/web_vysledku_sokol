from django.contrib import admin
from .models import Utkani, UtkaniAdmin, Tabulka, Rozpis

admin.site.register(Utkani, UtkaniAdmin)
admin.site.register(Tabulka)
admin.site.register(Rozpis)