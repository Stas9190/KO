from django.contrib import admin
from .models import Equipment, Unit, Untigroup

admin.site.register(Equipment)
admin.site.register(Unit)
#admin.site.register(Junction)
admin.site.register(Untigroup)