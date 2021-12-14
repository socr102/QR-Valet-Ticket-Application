from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Valet)
admin.site.register(Customer)
admin.site.register(Supervisor)
admin.site.register(VehicleColor)
admin.site.register(VehicleMake)
admin.site.register(CompanyPhoneNumber)
admin.site.register(Status)
admin.site.register(VehicleTracker)
admin.site.register(Usertype)
admin.site.register(UserProfile)
admin.site.register(TenantTable)


