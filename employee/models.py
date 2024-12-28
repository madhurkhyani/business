from django.db import models

# Create your models here.
class employee_data(models.Model):
    Name = models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")
    Salary=models.IntegerField()
    Joining_Date=models.DateField(auto_now=False, auto_now_add=False)
    note = models.CharField(max_length=250, default="No Note yet!")