from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse, reverse_lazy
# Create your models here.
class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    Nearest_city = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Service Providers"

    def get_absolute_url(self):
        return reverse("providers")
    


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.FloatField(default=0)
    service_image = models.ImageField(upload_to="services/images")
    date_created = models.DateTimeField(default=timezone.now)
    availability = models.CharField(max_length=200, default="24 Hours")
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name + str(self.cost)

    class Meta:
        verbose_name_plural = "Services"

    def get_absolute_url(self):
        return reverse("services")

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Product Categories"

    def get_absolute_url(self):
        return reverse("categories")

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Product Sub-Categories"

    def get_absolute_url(self):
        return reverse("subcategories")

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.FloatField()
    product_image = models.ImageField(upload_to="products/images")
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products")

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class County(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Counties"

    def get_absolute_url(self):
        return reverse("counties")

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    date_of_birth = models.DateTimeField()
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, default="Kenya")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("customers")

    def get_address(self):
        return self.postal_code + "-"+self.zip_code + " , "+self.city + "-"+self.country

class EmergencyContact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    relationship = models.CharField(max_length=200, default="Parent")
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, default="Kenya")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Emergency Contacts"

    def get_absolute_url(self):
        return reverse("emergencycontacts")

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Staff Members"

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer) + str(self.service)

    def get_absolute_url(self):
        return reverse("bookings")

    def accepted_text(self):
        if self.accepted:
            return "Accepted"
        else:
            return "Not Accepted"

