from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="home"),

    #ALL LISTS
    path("providers/", views.ProviderList, name="providers"),
    path("services/", views.ServiceList, name="services"),
    path("products/", views.ProductList, name="products"),
    path("counties/", views.CountyList, name="counties"),
    path("emergencycontacts/", views.EmergencyContactList, name="emergencycontacts"),
    path("bookings/", views.BookingList, name="boookings"),
    path("staff/", views.StaffList, name="staff"),
    path("roles/", views.RoleList, name="roles"),
    path("categories/", views.CategoryList, name="categories"),
    path("subcategories/", views.SubCategoryList, name="subcategories"),
    path("customers/", views.CustomerList, name="customers"),

    #CREATE URLS
    #UPDATE URLS
    #DELETE URLS
    #DETAILS URLS
    path("provider-details/<str:pk>/", views.ProviderDetail, name="provider-details"),
    path("service-details/<str:pk>/",
         views.ServiceDetail, name="service-details"),
    path("product-details/<str:pk>/",
         views.ProductDetail, name="product-details"),
    path("customer-details/<str:pk>/",
         views.CustomerDetail, name="customer-details"),
    path("category-details/<str:pk>/",
         views.CategoryDetail, name="category-details"),
    path("subcategory-details/<str:pk>/",
         views.SubCategoryDetail, name="subcategory-details"),
    path("emergencycontact-details/<str:pk>/",
         views.EmergencyContactDetail, name="emergencycontact-details"),
    path("county-details/<str:pk>/", views.CountyDetail, name="county-details"),
    path("booking-details/<str:pk>/",
         views.BookingDetail, name="booking-details"),
    path("role-details/<str:pk>/",
         views.RoleDetail, name="role-details"),
    path("staff-details/<str:pk>/",
         views.StaffDetail, name="staff-details"),
]
