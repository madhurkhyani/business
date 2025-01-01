from django.db import models

class ClientData(models.Model):
    Name = models.CharField(max_length=100)
    Company_Name = models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")
    email = models.EmailField()
    note = models.CharField(max_length=250, default="No Note yet!")

    def __str__(self):
        return self.Name