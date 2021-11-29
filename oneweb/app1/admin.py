from django.contrib import admin
from app1.models import Student

# Register your models here.

class Stud_Admin(admin.ModelAdmin):
    list_display = ['sno','sname','scourse']

admin.site.register(Student,Stud_Admin)
