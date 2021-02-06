from django.contrib import admin
from CBVAPP.models import Student
class StudentAdmin(admin.ModelAdmin):
    l=["name","number","marks","place"]
admin.site.register(Student,StudentAdmin)

# Register your models here.
