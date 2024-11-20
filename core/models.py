from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (('Admin', 'Admin'), ('HR', 'HR'), ('Employee', 'Employee'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Employee')

    # Override related_name for groups and permissions to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Custom related_name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",  # Custom related_name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

# Employee Data
class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    joining_date = models.DateField()

# Attendance Records
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

# Salary Information
class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    base_pay = models.FloatField()
    deductions = models.FloatField()
    net_salary = models.FloatField()
    payment_date = models.DateField()

# Holiday List
class Holiday(models.Model):
    date = models.DateField()
    reason = models.CharField(max_length=200)
