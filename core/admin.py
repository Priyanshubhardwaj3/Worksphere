from django.contrib import admin
from .models import CustomUser, Employee, Attendance, Salary, Holiday

admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(Holiday)
