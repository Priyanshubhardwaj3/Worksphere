from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # Root URL
    path('', views.home, name='home'),  # This will handle requests to the root URL

    # Dashboard URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('hr_dashboard/', views.hr_dashboard, name='hr_dashboard'),

    # Authentication URLs
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout page

    # Employee Management URLs
    path('manage-employees/', views.manage_employees, name='manage_employees'),
    path('add-employee/', views.add_employee, name='add_employee'),

    # Admin URLs
      # Admin panel URL
]



