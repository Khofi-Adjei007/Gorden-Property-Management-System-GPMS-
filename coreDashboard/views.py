from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .landlordRegistrationsForms import landlordRegistrationsForm
from django.contrib.auth.models import User
from .models import Landlord

# Create your views here.
def home(request):
    return render(request, 'home.html')


@csrf_protect
def createAccount(request):
    if request.method == "POST":
        form = landlordRegistrationsForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            user, created = User.objects.get_or_create(username=form_data['username'], email=form_data['email'])
            if created:
                user.set_password(form_data['password'])
                user.save()

            # Save the form data to the LandlordRegistration model
            Landlord.objects.create(
                first_name=form_data['first_name'],
                middle_name=form_data['middle_name'],
                last_name=form_data['last_name'],
                phone=form_data['phone'],
                email=form_data['email'],
                physical_address=form_data['physical_address'],
                Digital_address=form_data['Digital_address'],
                city_or_town=form_data['cityOrTown'],
                state_or_region=form_data['stateOrRegion'],
                country=form_data['country'],
                profile_photo=request.FILES['profile_photo']
            )
            # You might want to redirect after successful form submission
            #return redirect('some_view_name')
    else:
        form = landlordRegistrationsForm()
    
    return render(request, 'createAccount.html', {"form": form})



def login(request):
    return render(request, 'login.html')