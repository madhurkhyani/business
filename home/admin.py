from django.contrib import admin
from .models import Cash_in, Cash_out, Sales
# Register your models here.

class cashIn(admin.ModelAdmin):
    list_filter = ("date",)
    list_display = ("description", "amount", "date",)

class cashOut(admin.ModelAdmin):
    list_filter = ("date",)
    list_display = ("description", "amount", "date",)

class SALES(admin.ModelAdmin):
    list_filter = ("date",)
    list_display = ("description", "amount", "date",)

admin.site.register(Cash_in, cashIn)
admin.site.register(Cash_out, cashOut)
admin.site.register(Sales, SALES)
