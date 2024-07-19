from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .landlordRegistrationsForms import landlordRegistrationsForm
from .OrganizationsRegistrations import OrganizationsRegistrations
from django.contrib.auth.models import User
from .models import Landlord, Organization
from django.shortcuts import redirect
from django.http import HttpResponseForbidden





# Create your views here.
def home(request):
    return render(request, 'home.html')


@csrf_protect
def create_account(request):
    if request.method == "POST":
        if 'solo' in request.POST:
            form = landlordRegistrationsForm(request.POST, request.FILES)
            if form.is_valid():
                form_data = form.cleaned_data
                user, created = User.objects.get_or_create(username=form_data['username'], email=form_data['email'])
                if created:
                    user.set_password(form_data['password'])
                    user.save()
                    
                # Save the form data to the Landlord model
                Landlord.objects.create(
                    Given_name=form_data['Given_name'],
                    last_name=form_data['last_name'],
                    email=form_data['email'],
                    phone=form_data['phone'],
                    physical_address=form_data['physical_address'],
                    Digital_address=form_data['Digital_address'],
                    city_or_town=form_data['city_or_town'],
                    state_or_region=form_data['state_or_region'],
                    country=form_data['country'],
                    profile_photo=request.FILES['profile_photo']
                )
                # Redirect after successful form submission
                # return redirect('some_view_name') 
            else:
                solo_form = form  
                Organization_form = OrganizationsRegistrations()  

        elif 'Organization' in request.POST:
            form = OrganizationsRegistrations(request.POST, request.FILES)
            if form.is_valid():
                form_data = form.cleaned_data
                user, created = User.objects.get_or_create(username=form_data['username'], email=form_data['email'])
                if created:
                    user.set_password(form_data['password'])
                    user.save()

                # Save the form data to the Organization model
                Organization.objects.create(
                    OrganizationName=form_data['OrganizationName'],
                    OrganizationType=form_data['OrganizationType'],
                    NumberOfEmployees=form_data['NumberOfEmployees'],
                    OrganizationEmail=form_data['OrganizationEmail'],
                    OrganizationPhone=form_data['OrganizationPhone'],
                    OrganizationAddress=form_data['OrganizationAddress'],
                    Registration_Number=form_data['Registration_Number'],
                    OrganizationDigitalAddress=form_data['OrganizationDigitalAddress'],
                    Organization_City_Of_Operation=form_data['Organization_City_Of_Operation'],
                    OrganizationStateOrRegion=form_data['OrganizationStateOrRegion'],
                    OrganizationLogo=request.FILES['OrganizationLogo']
                )
                # Redirect after successful form submission
                # return redirect('some_view_name')
            else:
                Organization_form = form  # Keep the form with errors
                solo_form = landlordRegistrationsForm()  # Reset the other form
    else:
        solo_form = landlordRegistrationsForm()
        Organization_form = OrganizationsRegistrations()
    
    return render(request, 'createAccount.html', {
        "solo_form": solo_form,
        "organization_form": Organization_form
    })





@csrf_protect
def login(request):
    return render(request, 'login.html')