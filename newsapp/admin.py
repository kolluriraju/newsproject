from django.contrib import admin
from newsapp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','marks','rank','subject']
admin.site.register(Student,StudentAdmin)
