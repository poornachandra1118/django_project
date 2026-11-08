from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Courses)

admin.site.register(Student_details)

admin.site.register(Topic_videos)
admin.site.register(Course_type)