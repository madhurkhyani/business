from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.edit import CreateView
from .models import employee_data
from .forms import EmployeeDataForm
from django.http import HttpResponse

# Create your views here.



class Employee_page(CreateView):
    model=employee_data
    fields = ['Name', 'image', 'Salary', 'Joining_Date','note']
    template_name="employee/employee_page.html"
    context_object_name="employee_info"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_info'] = employee_data.objects.all()  # Fetch all records
        return context
    

class Add_employee(CreateView):
    template_name="employee/add_employee.html"
    model=employee_data
    form_class = EmployeeDataForm
    success_url="/employee"

def employee_detail(request,object_id):
    employee_detail=get_object_or_404(employee_data,id=object_id)
    return render(request,"employee/employee_detail.html",{
        "employee_detail" : employee_detail
    })

def delete_employee(request,object_id):
     employee_detail=get_object_or_404(employee_data,id=object_id)
     employee_detail.delete()
     return  redirect('employee_page')


def update_note(request, employee_id):
    # Retrieve the employee object or return a 404 if not found
    employee = get_object_or_404(employee_data, pk=employee_id)

    if request.method == 'POST':
        # Get the new note value from the form data
        new_note = request.POST.get('note')

        # Update the 'note' field with the new value
        employee.note = new_note

        # Save the updated employee data
        employee.save()

        # Redirect to the employee detail page or any other page
        return redirect('employee_detail', employee.id)

    return render(request, 'employee/update_note.html', {'employee': employee})


