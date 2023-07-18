from django.contrib import admin

# Register your models here.
from services.models import Service, Plan, Subscripthion


# Register your models here.

admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subscripthion)