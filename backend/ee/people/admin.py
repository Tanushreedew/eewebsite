from django.contrib import admin
from .models import Staff,Faculty,Phd,MTech,BTech,Alumni,MS
# Register your models here.

admin.site.register(Staff)
admin.site.register(Faculty)
admin.site.register(Phd)
admin.site.register(MTech)
admin.site.register(BTech)
admin.site.register(Alumni)
admin.site.register(MS)