from django.contrib import admin
from .models import Duty, Order, Leave

# Register your models here.
admin.site.register(Duty)
admin.site.register(Order)
admin.site.register(Leave)
