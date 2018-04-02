from django.contrib import admin
from .models import Equipment, Unit, Untigroup, Work

admin.site.register(Equipment)
admin.site.register(Unit)
admin.site.register(Work)
admin.site.register(Untigroup)