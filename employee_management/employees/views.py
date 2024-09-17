from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm

#Create your views here.

# Add Employee

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():  # Corrected method to validate the form
            form.save()
            messages.success(request, "Employee added successfully!")
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})


# Update Employee
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        form.fields['salary'].widget.attrs['readonly'] = True
        form.fields['designation'].widget.attrs['readonly'] = True
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully!")
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form})

# Delete Employee
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect('home')
    return render(request, 'employees/delete_employee.html', {'employee': employee})

# List All Employees (Home Page)
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})