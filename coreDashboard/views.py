from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .landlordRegistrationsForms import landlordRegistrationsForm
from .OrganizationsRegistrations import OrganizationsRegistrations
from django.contrib.auth.models import User
from .models import Landlord, Organization
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.contrib import messages





# Create your views here.
def home(request):
    return render(request, 'home.html')


@csrf_protect
def create_account(request):
    if request.method == "POST":
        if 'solo' in request.POST:
            solo_form = landlordRegistrationsForm(request.POST, request.FILES)
            Organization_form = OrganizationsRegistrations()  # Reset the organization form

            if solo_form.is_valid():
                form_data = solo_form.cleaned_data
                user, created = User.objects.get_or_create(username=form_data['username'], email=form_data['email'])
                if created:
                    user.set_password(form_data['password'])
                    user.save()

                # Save the form data to the Landlord model
                Landlord.objects.create(
                    user=user,
                    given_name=form_data['first_name'],
                    last_name=form_data['last_name'],
                    email=form_data['email'],
                    phone=form_data['phone'],
                    physical_address=form_data['physical_address'],
                    Digital_address=form_data['digital_address'],
                    cityOrTown=form_data['city_or_town'],
                    stateOrRegion=form_data['state_or_region'],
                    country=form_data['country'],
                    profile_photo=request.FILES['profile_photo']
                )
                messages.success(request, 'Registration successful!')
                return redirect('some_view_name')  # Adjust the redirect as needed
            else:
                # Form is not valid, re-render the page with errors
                messages.error(request, 'There were errors in your form submission.')

        elif 'Organization' in request.POST:
            solo_form = landlordRegistrationsForm()  # Reset the solo form
            Organization_form = OrganizationsRegistrations(request.POST, request.FILES)

            if Organization_form.is_valid():
                form_data = Organization_form.cleaned_data
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
                messages.success(request, 'Registration successful!')
                return redirect('some_view_name')  # Adjust the redirect as needed
            else:
                # Form is not valid, re-render the page with errors
                messages.error(request, 'There were errors in your form submission.')

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