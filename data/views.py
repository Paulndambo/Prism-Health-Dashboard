from django.shortcuts import render
from . models import Provider, Product, EmergencyContact, Staff, Role, Category, Service, SubCategory, County, Customer, Booking
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
# Create your views here.
def home(request):
    return render(request, "index.html")

def dailyReport(request):
    return render(request, "reports/daily.html")

def weeklyReport(request):
    return render(request, "reports/weekly.html")

def monthlyReport(request):
    return render(request, "reports/monthly.html")

def annualReport(request):
    return render(request, "reports/annual.html")

class ProvidersList(ListView):
    model = Provider
    template_name = "dashboard/providers.html"

class CreateProvider(CreateView):
    model = Provider
    fields = '__all__'
    template_name = "dashboard/add_provider.html"

class ProviderDetails(DetailView):
    model = Provider
    template_name = "dashboard/provider_details.html"

class StaffsList(ListView):
    model = Staff
    template_name = "dashboard/staff.html"

class CreateStaff(CreateView):
    model = Staff
    fields = '__all__'
    template_name = "dashboard/add_staff.html"

class RolesList(ListView):
    model = Role
    template_name = "dashboard/roles.html"

class CreateRole(CreateView):
    model = Role
    fields = '__all__'
    template_name = "dashboard/add_role.html"

class ServicesList(ListView):
    model = Service
    template_name = "dashboard/services.html"

class CreateService(CreateView):
    model = Service
    fields = '__all__'
    template_name = "dashboard/add_service.html"

class ServiceDetails(DetailView):
    model = Service
    template_name = "dashboard/service_details.html"

class CategoriesList(ListView):
    model = Category
    template_name = "dashboard/categories.html"

class CreateCategory(CreateView):
    model = Category
    fields = '__all__'
    template_name = "dashboard/add_category.html"

class CategoryDetails(DetailView):
    model = Category
    template_name = "dashboard/category_details.html"

class SubCategoriesList(ListView):
    model = SubCategory
    template_name = "dashboard/subcategories.html"

class CreateSubCategory(CreateView):
    model = SubCategory
    fields = '__all__'
    template_name = "dashboard/add_subcategory.html"

class SubCategoryDetails(DetailView):
    model = SubCategory
    template_name = "dashboard/subcategory_details.html"

class ProductsList(ListView):
    model = Product
    template_name = "dashboard/products.html"

class CreateProduct(CreateView):
    model = Product
    fields = '__all__'
    template_name = "dashboard/add_product.html"

class ProductDetails(DetailView):
    model = Product
    template_name = "dashboard/product_details.html"

class CountiesList(ListView):
    model = County
    template_name = "dashboard/counties.html"

class CreateCounty(CreateView):
    model = County
    fields = '__all__'
    template_name = "dashboard/add_county.html"

class CountyDetails(DetailView):
    model = County
    template_name = "dashboard/county_details.html"

class CustomersList(ListView):
    model = Customer
    template_name = "dashboard/customers.html"

class CreateCustomer(CreateView):
    model = Customer
    fields = '__all__'
    template_name = "dashboard/add_customer.html"

class CustomerDetails(DetailView):
    model = Customer
    template_name = "dashboard/customer_details.html"

class EmergencyContactsList(ListView):
    model = EmergencyContact
    template_name = "dashboard/emergencycontacts.html"

class CreateEmergencyContact(CreateView):
    model = EmergencyContact
    fields = '__all__'
    template_name = "dashboard/add_emergencycontact.html"

class EmergencyContactDetails(DetailView):
    model = EmergencyContact
    template_name = "dashboard/emergencycontact_details.html"

class BookingsList(ListView):
    model = Booking
    template_name = "dashboard/bookings.html"


class CreateBooking(CreateView):
    model = Booking
    fields = '__all__'
    template_name = "dashboard/add_booking.html"


class BookingDetails(DetailView):
    model = Booking
    template_name = "dashboard/booking_details.html"
