from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid', 'cname', 'cadd', 'cmail']

admin.site.register(Customer, CustomerAdmin)