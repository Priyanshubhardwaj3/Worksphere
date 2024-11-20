from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Employee, Attendance, Salary, Holiday
from .forms import EmployeeForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm

# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Login view using Django's built-in AuthenticationForm
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page or another page after login
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def user_logout(request):
    logout(request)
    return redirect('login')
@login_required
def employee_dashboard(request):
    if request.user.role == 'Employee':  # Check if the user is an employee
        attendance = Attendance.objects.filter(employee=request.user.employee)
        salary = Salary.objects.filter(employee=request.user.employee)
        holidays = Holiday.objects.all()
        
        return render(request, 'core/employee_dashboard.html', {
            'attendance': attendance,
            'salary': salary,
            'holidays': holidays
        })
    else:
        return redirect('no_permission')  # Redirect if user is not an employee
# In views.py

from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')  # or whatever your dashboard template is

def dashboard(request):
    # Check user role and redirect to corresponding dashboard
    if request.user.is_authenticated:
        if request.user.role == 'Admin':
            return redirect('admin_dashboard')
        elif request.user.role == 'HR':
            return redirect('hr_dashboard')
        elif request.user.role == 'Employee':
            return redirect('employee_dashboard')
        else:
            return redirect('login')
    else:
        return redirect('login')  # Redirect to login if not authenticated

from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    if request.user.role == 'Admin':  # Ensuring the user is an Admin
        employees = Employee.objects.all()  # Get all employees
        return render(request, 'core/admin_dashboard.html', {'employees': employees})
    else:
        return redirect('no_permission')  # Redirect if the user isn't an Admin


@login_required
def hr_dashboard(request):
    if request.user.role == 'HR':  # Check if user is HR
        employees = Employee.objects.all()  # Get all employees data
        return render(request, 'core/hr_dashboard.html', {'employees': employees})
    else:
        return redirect('no_permission')  # Redirect if not HR


from .forms import EmployeeForm

@login_required
def manage_employees(request):
    if request.user.role == 'Admin':
        employees = Employee.objects.all()  # List all employees
        return render(request, 'core/manage_employees.html', {'employees': employees})
    else:
        return redirect('no_permission')  # Redirect if not admin

@login_required
def add_employee(request):
    if request.user.role == 'Admin':
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()  # Save the employee data to the database
                return redirect('manage_employees')  # Redirect to employee list after adding
        else:
            form = EmployeeForm()
        return render(request, 'core/add_employee.html', {'form': form})
    else:
        return redirect('no_permission')  # Redirect if not admin

@login_required
def attendance_report(request):
    attendance = Attendance.objects.all()
    report = {}
    for record in attendance:
        if record.employee not in report:
            report[record.employee] = {'Present': 0, 'Absent': 0}
        report[record.employee][record.status] += 1
    return render(request, 'core/attendance_report.html', {'report': report})

from django.shortcuts import redirect

def role_required(role):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.role == role:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('no_permission')  # Redirect if the user doesn't have the required role
        return wrapper
    return decorator
@role_required('Admin')
def admin_dashboard(request):
    employees = Employee.objects.all()  # Get all employees
    return render(request, 'core/admin_dashboard.html', {'employees': employees})

from django.core.mail import send_mail

def send_salary_email(employee, salary_details):
    send_mail(
        subject='Your Salary Details',
        message=f'Dear {employee.user.first_name},\n\nYour salary for this month is ₹{salary_details["net_salary"]}.',
        from_email='admin@worksphere.com',
        recipient_list=[employee.user.email],
    )
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # You can customize the template name

# views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')  # Correctly specify the path


@login_required
def dashboard(request):
    employee_data = {
        'name': request.user.username,
        'email': request.user.email,
        'attendance': 25,  # Example attendance data
        'leaves': 5,
    }
    return render(request, 'dashboard.html', {'employee': employee_data})
