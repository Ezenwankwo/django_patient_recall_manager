from django.contrib import admin

# Register your models here.

from .models import Schedule
from .models import Patient


admin.site.register(Schedule)
admin.site.register(Patient)
