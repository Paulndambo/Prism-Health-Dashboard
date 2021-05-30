from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from data.models import Provider, Service, Category, SubCategory, Product, County, Customer, EmergencyContact, Role, Staff, Booking

from . serializers import ProviderSerializer, ServiceSerializer, CategorySerializer, SubCategorySerializer, ProductSerializer, CustomerSerializer
from . serializers import EmergencyContactSerializer, RoleSerializer, StaffSerializer, BookingSerializer, CountySerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {

        #Provider Endpoints
        'Providers': '/providers/',
        'Provider Detail': '/provider-details/<str:pk>/',
        'Create Provider': '/create-provider/',
        'Update Provider': '/update-provider/<str:pk>/',
        'Delete Provider': '/delete-provider/<str:pk>/',

        #Service Endpoints
        'Services': '/services/',
        'Service Details': '/service-details/<str:pk>/',
        'Create Service': '/create-service/',
        'Update Service': '/update-service/<str:pk>/',
        'Delete Service': '/delete-service/<str:pk>/',

        #Category Endpoints
        'Categories': '/categories/',
        'Category Details': 'category-details/<str:pk>/',
        'Create Category': '/create-category/',
        'Update Category': '/update-category/<str:pk>/',
        'Delete Category': '/delete-category/<str:pk>/',

        #Sub-Category Endpoints
        'SubCategories': '/subcategories/',
        'SubCategory Details': '/SubCategory-details/<str:pk>/',
        'Create SubCategory': '/create-SubCategory/',
        'Update SubCategory': '/update-SubCategory/<str:pk>/',
        'Delete SubCategory': '/delete-SubCategory/<str:pk>/',

        #County Endpoints
        'Counties': '/counties/',
        'County Details': '/county-details/<str:pk>/',
        'Create County': '/create-service/',
        'Update County': '/update-service/<str:pk>/',
        'Delete County': '/delete-service/<str:pk>/',

        #Customer Endpoints
        'Customers': '/customers/',
        'Customer Details': 'customer-details/<str:pk>/',
        'Create Customer': '/create-customer/',
        'Update Customer': '/update-customer/<str:pk>/',
        'Delete Customer': '/delete-customer/<str:pk>/',

        #Product Endpoints
        'Products': '/products/',
        'Product Details': 'product-details/<str:pk>/',
        'Create Product': '/create-product/',
        'Update Product': '/update-product/<str:pk>/',
        'Delete Product': '/delete-product/<str:pk>/',

        #Emergency Contact Endpoints
        'Emergency Contacts': '/emergency-contacts/',
        'Emergency Contact Details': 'emergencycontact-details/<str:pk>/',
        'Create Emergency Contact': '/create-emergencycontact/',
        'Update Emergency Contact': '/update-emergencycontact/<str:pk>/',
        'Delete Emergency Contact': '/delete-emergencycontact/<str:pk>/',

        #Staff Endpoints
        'Staff': '/staff/',
        'Staff Details': '/role-details/<str:pk>/',
        'Create Staff': '/create-role/',
        'Update Staff': '/update-role/<str:pk>/',
        'Delete Staff': '/delete-role/<str:pk>/',

        #Staff Roles Endpoints
        'Staff Roles': '/roles/',
        'Role Details': 'role-details/<str:pk>/',
        'Create Role': '/create-role/',
        'Update Role': '/update-role/<str:pk>/',
        'Delete Role': '/delete-role/<str:pk>/',

        #Booking Endpoints
        'Bookings': '/bookings/',
        'Booking Details': 'booking-details/<str:pk>/',
        'Create Booking': '/create-booking/',
        'Update Booking': '/update-booking/<str:pk>/',
        'Delete Booking': '/delete-booking/<str:pk>/',
    }
    return Response(api_urls)


#GET Endpoints
@api_view(['GET'])
def ProviderList(request):
    providers = Provider.objects.all().order_by('-id')
    serializer = ProviderSerializer(providers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ServiceList(request):
    services = Service.objects.all().order_by('-id')
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def EmergencyContactList(request):
    emergencycontacts = EmergencyContact.objects.all().order_by('-id')
    serializer = EmergencyContactSerializer(emergencycontacts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CountyList(request):
    counties = County.objects.all().order_by('-id')
    serializer = CountySerializer(counties, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CategoryList(request):
    categories = Category.objects.all().order_by('-id')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def SubCategoryList(request):
    subcategories = SubCategory.objects.all().order_by('-id')
    serializer = SubCategorySerializer(subcategories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductList(request):
    products = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CustomerList(request):
    customers = Customer.objects.all().order_by('-id')
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def StaffList(request):
    staff = Staff.objects.all().order_by('-id')
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def RoleList(request):
    roles = Role.objects.all().order_by('-id')
    serializer = RoleSerializer(roles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def BookingList(request):
    bookings = Booking.objects.all().order_by('-id')
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

#Create Endpoints
#Detail Endpoints
@api_view(['GET'])
def ProviderDetail(request, pk):
    provider = Provider.objects.get(id=pk)
    serializer = ProviderSerializer(provider, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def ServiceDetail(request, pk):
    service = Service.objects.get(id=pk)
    serializer = ServiceSerializer(service, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def ProductDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def CustomerDetail(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def EmergencyContactDetail(request, pk):
    emergencycontact = EmergencyContact.objects.get(id=pk)
    serializer = EmergencyContactSerializer(emergencycontact, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def CategoryDetail(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def SubCategoryDetail(request, pk):
    subcategory = SubCategory.objects.get(id=pk)
    serializer = SubCategorySerializer(subcategory, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def CountyDetail(request, pk):
    county = County.objects.get(id=pk)
    serializer = CountySerializer(county, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def RoleDetail(request, pk):
    role = Role.objects.get(id=pk)
    serializer = RoleSerializer(role, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def StaffDetail(request, pk):
    staff = Staff.objects.get(id=pk)
    serializer = StaffSerializer(staff, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def BookingDetail(request, pk):
    booking = Booking.objects.get(id=pk)
    serializer = BookingSerializer(booking, many=False)
    return Response(serializer.data)
