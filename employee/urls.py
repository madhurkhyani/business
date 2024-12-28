from django.urls import  path
from . import views
from .views import Add_employee
urlpatterns = [
    path("", views.Employee_page.as_view(), name='employee_page'),
    path("add_employee", views.Add_employee.as_view(), name="add_employee"),
    path("employee_detail/<int:object_id>", views.employee_detail, name="employee_detail"),
    path("delete_employee/<int:object_id>", views.delete_employee, name="delete_employee"),
    path('update_note/<int:employee_id>/', views.update_note, name='update_note')
]
