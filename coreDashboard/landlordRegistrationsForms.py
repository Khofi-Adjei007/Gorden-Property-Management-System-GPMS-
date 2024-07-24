from django import forms
import re
import string
from .models import Landlord

class landlordRegistrationsForm(forms.Form):
    given_name = forms.CharField(max_length=200, label='Given Name(s)', error_messages={'required': 'We Need a Given Name', 'invalid': 'The Input is Invalid Actually'})
    def clean_given_name(self):
        given_name = self.cleaned_data['given_name']
        if not re.match(r'^[a-zA-Z]*$', given_name):
            raise forms.ValidationError('Enter a valid first name.')
        return given_name
    
    last_name = forms.CharField(max_length=200, label='Last Name', error_messages={'required': 'We Need A Last Name Too.', 'invalid': 'The Input is Invalid Actually'})
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.match(r'^[a-zA-Z]*$', last_name):
            raise forms.ValidationError('Enter a valid last name.')
        return last_name
    
    phone = forms.CharField(max_length=200, label='Phone Number', error_messages={'required': 'Phone Number is Required.', 'invalid': 'Phone Number is Invalid.'})
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^[0-9]*$', phone):
            raise forms.ValidationError('Enter a valid phone number.')
        return phone
    
    email = forms.EmailField(label='Email Address', error_messages={'required': 'Email is Required.', 'invalid': 'Email is Invalid.'})
    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise forms.ValidationError('Enter a valid email address.')
        return email

    physical_address = forms.CharField(max_length=200, label='Physical Address', error_messages={'required': 'Physical Address is Required.', 'invalid': 'Address is Invalid.'})    
    def clean_physical_address(self):
        physical_address = self.cleaned_data['physical_address']
        return physical_address
    
    digital_address = forms.CharField(max_length=200, label='Digital Address', error_messages={'required': 'Digital Address is Required.', 'invalid': 'Address is Invalid.'})
    def clean_digital_address(self):
        digital_address = self.cleaned_data['digital_address']
        return digital_address
    
    city_or_town = forms.CharField(max_length=200, label='City or Town', error_messages={'required': 'City or Town is Required.', 'invalid': 'City or Town is Invalid.'})
    def clean_city_or_town(self):
        city_or_town = self.cleaned_data['city_or_town']
        return city_or_town
    
    state_or_region = forms.CharField(max_length=200, label='State or Region', error_messages={'required': 'State or Region is Required.', 'invalid': 'State or Region is Invalid.'})
    def clean_state_or_region(self):
        state_or_region = self.cleaned_data['state_or_region']
        return state_or_region
    
    profile_photo = forms.ImageField(label='Profile Photo', error_messages={'required': 'Profile Photo Cannot Be Empty', 'invalid': 'Invalid Upload'})
    def clean_profile_photo(self):
        profile_photo = self.cleaned_data['profile_photo']
        return profile_photo
    
    country = forms.CharField(max_length=200, label='Country', error_messages={'required': 'Country Field Is Required', 'invalid': 'Invalid Country Selection'})
    def clean_country(self):
        country = self.cleaned_data['country']
        return country
    
    password = forms.CharField(max_length=200, label='Password', error_messages={'required': 'Password is Required.', 'invalid': 'Password Input Is Invalid'})
    def clean_password(self):
        password = self.cleaned_data.get('password')
        criteria = {'special': set(string.punctuation), 'numeric': set(string.digits), 'uppercase': set(string.ascii_uppercase)}
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        if not any(char in criteria['special'] for char in password) or \
           not any(char in criteria['numeric'] for char in password) or \
           not any(char in criteria['uppercase'] for char in password):
            raise forms.ValidationError('Password is weak, Try Again')
        return password
    
    confirm_password = forms.CharField(max_length=200, label='Confirm Password', error_messages={'required': 'Ooops! Please Confirmed Password.', 'invalid': 'Password is Invalid.'})
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return confirm_password
