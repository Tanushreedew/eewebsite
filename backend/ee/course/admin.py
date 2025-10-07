from django.contrib import admin
from .models import Elective, Course, CourseNew
# Register your models here.

admin.site.register(Elective)
admin.site.register(Course)
admin.site.register(CourseNew)