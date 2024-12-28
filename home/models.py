from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator

# Create your models here.

class Cash_in(models.Model):
    amount=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    description=models.TextField()
    date=models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.amount} {self.description}"
    
class Cash_out(models.Model):
    amount=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    description=models.TextField()
    date=models.DateField(auto_now=True)


class Sales(models.Model):
    amount=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    description=models.TextField()
    date=models.DateField(auto_now=True)
