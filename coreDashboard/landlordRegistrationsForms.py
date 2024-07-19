from django.db import models
from .models import Landlord
from django import forms
import re
import string


#Landlords | Property Managers  | Asset Managers | Property Owners Registrations and Authentication
class landlordRegistrationsForm(forms.Form):

    Given_name = forms.CharField(max_length=200, label='Given Name(s)', error_messages={'required': 'First Name is Required .',
                                                    'invalid': 'Name is Invalid.'})
    def clean_Given_name(self):
        Given_name = self.cleaned_data['first_name']
        if Given_name is None:
            raise forms.ValidationError('First Name is Required.')
        elif not re.match(r'^[a-zA-Z]*$', Given_name):
            raise forms.ValidationError(("Enter a valid first name."))
        return Given_name
    
    # middle_name = forms.CharField(max_length=200, label='Middle Name', required=False, error_messages={'invalid': 'Name is Invalid.'})
    # def clean_middle_name(self):
    #     middle_name = self.cleaned_data.get('middle_name')
    #     if middle_name and not re.match(r'^[a-zA-Z]*$', middle_name):
    #         raise forms.ValidationError(("Enter a valid middle name."))
    #     return middle_name
    
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
    
    digital_address = forms.CharField(max_length=200, label='Digital Address', error_messages={'required': 'Digital Address is Required .',
                                                    'invalid': 'Address is Invalid.'})
    def digital_address (self):
        digital_address = self.cleaned_data['Digital_address']
        if digital_address is None:
            raise forms.ValidationError('Digital Address is Required.')
        return digital_address
    
    CityOrTown = forms.CharField(max_length=200, label='City or Town', error_messages={'required': 'City or Town is Required .',
                                                    'invalid': 'City or Town is Invalid.'})
    def cityOrTown(self):
        cityOrTown = self.cleaned_data['cityOrTown']
        if cityOrTown is None:
            raise forms.ValidationError('City or Town is Required.')
        return cityOrTown
    
    StateOrRegion = forms.CharField(max_length=200, label='State or Region', error_messages={'required': 'State or Region is Required .',
                                                    'invalid': 'State or Region is Invalid.'})
    def stateOrRegion(self):
        stateOrRegion = self.cleaned_data['stateOrRegion']
        if stateOrRegion is None:
            raise forms.ValidationError('State or Region is Required.')
        return stateOrRegion
    
    Profile_photo = forms.ImageField(label='Profile Photo', error_messages={'required': 'Profile Photo is Required .',
                                                    'invalid': 'Photo is Invalid.'})
    def profile_photo(self):
        profile_photo = self.cleaned_data['profile_photo']
        if profile_photo is None:
            raise forms.ValidationError('Profile Photo is Required.')
        return profile_photo
    
    Country = forms.CharField(max_length=200, label='Country', error_messages={'required': 'Country is Required .',
                                                    'invalid': 'Country is Invalid.'})
    def country(self):
        country = self.cleaned_data['country']
        if country is None:
            raise forms.ValidationError('Country is Required.')
        return country
    
    password = forms.CharField(max_length=200, label='Password', error_messages={'required': 'Password is Required .',
                                                    'invalid': 'Password is Invalid.'})
    def clean_password(self):
        password = self.cleaned_data.get('password')
        criteria = {'special': set(string.punctuation), 'numeric': set(string.digits), 'uppercase': set(string.ascii_uppercase)}
        if len(password) < 8:
            raise forms.ValidationError(("Password must be at least 8 characters long."))
        if  any(not any(char in char_set for char in password) for char_type, char_set in criteria.items()):
            raise forms.ValidationError('Password is weak, Try Again')
        return password
    
    confirm_password = forms.CharField(max_length=200, label='Confirm Password', error_messages={'required': 'Ooops! Please Confirmed Password.',
                                                    'invalid': 'Password is Invalid.'})
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return confirm_password