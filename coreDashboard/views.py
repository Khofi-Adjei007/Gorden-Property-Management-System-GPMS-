from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .landlordRegistrationsForms import landlordRegistrationsForm
from django.contrib.auth.models import User

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

            first_name = form_data['first_name']
            middle_name = form_data['middle_name']
            last_name = form_data['last_name']
            phone = form_data['phone']
            email = form_data['email']
            physical_address = form_data['physical_address']
            Digital_address = form_data['Digital_address']
            cityOrTown = form_data['cityOrTown']
            stateOrRegion = form_data['stateOrRegion']
            country = form_data['country']
            profile_photo = request.FILES['profile_photo']
            
            # Additional logic to handle the collected data
            # For example, you might want to save it to a custom user profile model

            #return redirect('success_page')  # Redirect to a success page
    else:
        form = landlordRegistrationsForm()

    return render(request, 'createAccount.html', {"form": form})

 