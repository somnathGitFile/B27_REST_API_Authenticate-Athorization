from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'marks', 'addr']

admin.site.register(Student, StudentAdmin)