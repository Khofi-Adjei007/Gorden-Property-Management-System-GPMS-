from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


#Landlords | Property Managers  | Asset Managers | Property Owners
class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    given_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    physical_address = models.CharField(max_length=200)
    Digital_address = models.CharField(max_length=200)
    cityOrTown = models.CharField(max_length=200)
    stateOrRegion = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to='landlord/profile_photos')
    country = CountryField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


#Organizations | Companies | Institutions | Agencies
class Organization(models.Model):
    OrganizationName = models.CharField(max_length=200)
    OrganizationType = models.CharField(max_length=200)
    NumberOfEmployees = models.IntegerField()
    OrganizationEmail = models.EmailField()
    OrganizationPhone = models.CharField(max_length=200)
    OrganizationAddress = models.CharField(max_length=200)
    Registration_Number = models.CharField(max_length=250)
    OrganizationDigitalAddress = models.CharField(max_length=200)
    Organization_City_Of_Operation = models.CharField(max_length=200)
    OrganizationStateOrRegion = models.CharField(max_length=200)
    OrganizationLogo = models.ImageField(upload_to='organization/organization_logos')
    password = models.CharField(max_length=200)


#Properties | Buildings | Units | Rooms
class property(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    digita_address = models.CharField(max_length=200)
    mailing_address = models.CharField(max_length=200)
    cityOrTown = models.CharField(max_length=200)
    stateOrRegion = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    property_type = models.CharField(max_length=200)
    num_units = models.IntegerField()
    maintenance_status = models.CharField(max_length=200)
    property_photo = models.ImageField(upload_to='property/property_photos')
    property_video = models.FileField(upload_to='property/property_videos')
    property_amenities = models.TextField()
    property_amount = models.DecimalField(max_digits=10, decimal_places=2)
    lease_status = models.CharField(max_length=200)
    lease_start_date = models.DateField()
    lease_expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     
    def __str__(self):
        return self.name


#Tenants | Renters | Occupants
class Tenant(models.Model):
    property = models.ForeignKey(property, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    occupation = models.CharField(max_length=200)
    physical_address = models.CharField(max_length=200)
    Digital_address = models.CharField(max_length=200)
    cityOrTown = models.CharField(max_length=200)
    stateOrRegion = models.CharField(max_length=200)
    countryOfOrigin = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

