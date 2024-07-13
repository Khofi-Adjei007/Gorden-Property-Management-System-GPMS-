from django.db import models
from .models import Landlord
from django import forms
import re


#Landlords | Property Managers  | Asset Managers | Property Owners Registrations and Authentication
class landlordRegistrationsForm(forms.Form):
    first_name = forms.CharField(max_length=200, label='First Name', error_messages={'required': 'First Name is Required .',
                                                    'invalid': 'Name is Invalid.'})
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name is None:
            raise forms.ValidationError('First Name is Required.')
        elif not re.match(r'^[a-zA-Z]*$', first_name):
            raise forms.ValidationError(("Enter a valid first name."))
        return first_name
    
    middle_name = forms.CharField(max_length=200, label='Middle Name', required=False, error_messages={'invalid': 'Name is Invalid.'})
    def clean_middle_name(self):
        middle_name = self.cleaned_data.get('middle_name')
        if middle_name and not re.match(r'^[a-zA-Z]*$', middle_name):
            raise forms.ValidationError(("Enter a valid middle name."))
        return middle_name
    
    last_name = forms.CharField(max_length=200, label='Last Name', error_messages={'required': 'Last Name is Required .',
                                                    'invalid': 'Name is Invalid.'})
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name is None:
            raise forms.ValidationError('Last Name is Required.')
        elif not re.match(r'^[a-zA-Z]*$', last_name):
            raise forms.ValidationError(("Enter a valid last name."))
    
    phone = forms.CharField(max_length=200, label='Phone Number', error_messages={'required': 'Phone Number is Required .',
                                                    'invalid': 'Phone Number is Invalid.'})
    def clearn_phone(self):
        phone = self.cleaned_data['phone']
        if phone is None:
            raise forms.ValidationError('Phone Number is Required.')
        elif not re.match(r'^[0-9]*$', phone):
            raise forms.ValidationError(("Enter a valid phone number."))
        return phone
    
    email = forms.EmailField(label='Email Address', error_messages={'required': 'Email is Required .',
                                                    'invalid': 'Email is Invalid.'})
    def clean_email(self):
        email = self.cleaned_data['email']
        if email is None:
            raise forms.ValidationError('Email is Required.')
        elif not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise forms.ValidationError(("Enter a valid email address."))
        return email

    physical_address = forms.CharField(max_length=200, label='Physical Address', error_messages={'required': 'Physical Address is Required .',
                                                    'invalid': 'Address is Invalid.'})    
    def clean_physical_address(self):
        physical_address = self.cleaned_data['physical_address']
        if physical_address is None:
            raise forms.ValidationError('Physical Address is Required.')
        return physical_address 
    
    Digital_address = forms.CharField(max_length=200, label='Digital Address', error_messages={'required': 'Digital Address is Required .',
                                                    'invalid': 'Address is Invalid.'})
    def Digital_address (self):
        Digital_address = self.cleaned_data['Digital_address']
        if Digital_address is None:
            raise forms.ValidationError('Digital Address is Required.')
        return Digital_address
    
    cityOrTown = forms.CharField(max_length=200, label='City or Town', error_messages={'required': 'City or Town is Required .',
                                                    'invalid': 'City or Town is Invalid.'})
    def cityOrTown(self):
        cityOrTown = self.cleaned_data['cityOrTown']
        if cityOrTown is None:
            raise forms.ValidationError('City or Town is Required.')
        return cityOrTown
    
    stateOrRegion = forms.CharField(max_length=200, label='State or Region', error_messages={'required': 'State or Region is Required .',
                                                    'invalid': 'State or Region is Invalid.'})
    def stateOrRegion(self):
        stateOrRegion = self.cleaned_data['stateOrRegion']
        if stateOrRegion is None:
            raise forms.ValidationError('State or Region is Required.')
        return stateOrRegion
    
    profile_photo = forms.ImageField(label='Profile Photo', error_messages={'required': 'Profile Photo is Required .',
                                                    'invalid': 'Photo is Invalid.'})
    def profile_photo(self):
        profile_photo = self.cleaned_data['profile_photo']
        if profile_photo is None:
            raise forms.ValidationError('Profile Photo is Required.')
        return profile_photo
    
    country = forms.CharField(max_length=200, label='Country', error_messages={'required': 'Country is Required .',
                                                    'invalid': 'Country is Invalid.'})
    def country(self):
        country = self.cleaned_data['country']
        if country is None:
            raise forms.ValidationError('Country is Required.')
        return country