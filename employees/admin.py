from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_id','name','email','designation','department','salary']

admin.site.register(Employee,EmployeeAdmin)