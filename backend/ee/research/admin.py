from django.contrib import admin
from .models import Research, PGLabs, Papers, Projects, UGLabs
# Register your models here.

admin.site.register(Research)
admin.site.register(PGLabs)
admin.site.register(UGLabs)
admin.site.register(Papers)
admin.site.register(Projects)