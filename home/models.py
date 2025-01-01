from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from client.models import ClientData
# Create your models here.

class Cash_in(models.Model):
    amount=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    description=models.TextField()
    date=models.DateField(auto_now=True)
    client = models.ForeignKey(ClientData, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name_plural = 'Cash In'

    def __str__(self):
        return f"{self.amount} {self.description}"
    
class Cash_out(models.Model):
    amount=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    description=models.TextField()
    date=models.DateField(auto_now=True)
    client = models.ForeignKey(ClientData, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name_plural = 'Cash Out'

    def __str__(self):
        return f"{self.amount} {self.description}"


class Sales(models.Model):
    amount=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    description=models.TextField()
    date=models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Sales'

    def __str__(self):
        return f"{self.amount} {self.description}"
