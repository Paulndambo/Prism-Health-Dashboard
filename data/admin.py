from django.contrib import admin
from . models import Provider, Product, Category, Service, SubCategory, County, Customer, Booking, EmergencyContact
# Register your models here.
admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(County)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Service)
admin.site.register(EmergencyContact)


admin.site.site_header = "PRISM HEALTH ADMIN"
admin.site.site_title = "PRISM HEALTH ADMIN"
