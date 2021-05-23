from django.urls import path
from . import views
from . views import CreateProduct, CreateRole, CreateStaff, StaffsList, RolesList, ProvidersList, ServicesList, CustomersList, ProductsList, CategoriesList, SubCategoriesList, CountiesList, BookingsList, EmergencyContactsList, dailyReport
from . views import CreateProvider, CreateService, CreateCustomer, CreateCategory, CreateSubCategory, CreateCounty, CreateBooking, CreateEmergencyContact
from . views import ProviderDetails, ProductDetails, ServiceDetails, CustomerDetails, CategoryDetails, SubCategoryDetails, CountyDetails, EmergencyContactDetails, BookingDetails

urlpatterns = [
    path("", views.home, name="home"),

    #Reports
    path("daily/", views.dailyReport, name="daily"),
    path("weekly/", views.weeklyReport, name="weekly"),
    path("monthly/", views.monthlyReport, name="monthly"),
    path("annual/", views.annualReport, name="annual"),

    #List views/Urls
    path("providers/", ProvidersList.as_view(), name="providers"),
    path("products/", ProductsList.as_view(), name="products"),
    path("services/", ServicesList.as_view(), name="services"),
    path("customers/", CustomersList.as_view(), name="customers"),
    path("categories/", CategoriesList.as_view(), name="categories"),
    path("subcategories/", SubCategoriesList.as_view(), name="subcategories"),
    path("counties/", CountiesList.as_view(), name="counties"),
    path("bookings/", BookingsList.as_view(), name="bookings"),
    path("emergencycontacts/", EmergencyContactsList.as_view(), name="emergencycontacts"),
    path("staffs/", StaffsList.as_view(), name="staffs"),
    path("roles/", RolesList.as_view(), name="roles"),

    #Create Views/Urls
    path("create_provider/", CreateProvider.as_view(), name="create_provider"),
    path("create_service/", CreateService.as_view(), name="create_service"),
    path("create_product/", CreateProduct.as_view(), name="create_product"),
    path("create_customer/", CreateCustomer.as_view(), name="create_customer"),
    path("create_category/", CreateCategory.as_view(), name="create_category"),
    path("create_subcategory/", CreateSubCategory.as_view(), name="create_subcategory"),
    path("create_county/", CreateCounty.as_view(), name="create_county"),
    path("create_booking/", CreateBooking.as_view(), name="create_booking"),
    path("create_emergencycontact/", CreateEmergencyContact.as_view(), name="create_emergencycontact"),
    path("create_role/", CreateRole.as_view(), name="create_role"),
    path("create_staff/", CreateStaff.as_view(), name="create_staff"),

    #Details Views/Urls


]
