from django.contrib import admin
from .models import Interest
from .models import Course

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)

class CourseAdmin(admin.ModelAdmin):
	model = Course
#	readonly_fields = ('created_date', 'modified_date')

class InterestAdmin(admin.ModelAdmin):
	model = Interest
#	readonly_fields = ('created_date', 'modified_date')

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Interest, InterestAdmin)

