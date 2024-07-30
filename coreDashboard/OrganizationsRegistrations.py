from django.db import models
from .models import Organization
import re
from django import forms
import string


#Organizations | Companies | Institutions | Agencies Registrations and Authentication
class OrganizationsRegistrations(forms.Form):
    OrganizationName = forms.CharField(max_length=200, label='Organization Name', error_messages={'required': 'Organization Name is Required .',
                                                    'invalid': 'Name is Invalid.'})
    def clean_OrganizationName(self):
        OrganizationName = self.cleaned_data['OrganizationName']
        if OrganizationName is None:
            raise forms.ValidationError('Organization Name is Required.')
        elif not re.match(r'^[a-zA-Z]*$', OrganizationName):
            raise forms.ValidationError(("Enter a valid Organization name."))
        return OrganizationName
    
    OrganizationType = forms.CharField(max_length=200, label='Organization Type', error_messages={'required': 'Organization Type is Required .',
                                                    'invalid': 'Type is Invalid.'})
    def clean_OrganizationType(self):
        OrganizationType = self.cleaned_data['OrganizationType']
        if OrganizationType is None:
            raise forms.ValidationError('Organization Type is Required.')
        elif not re.match(r'^[a-zA-Z]*$', OrganizationType):
            raise forms.ValidationError(("Enter a valid Organization Type."))
        return OrganizationType
    
    OrganizationEmail = forms.EmailField(label='Organization Email Address', error_messages={'required': 'Email is Required .',
                                                    'invalid': 'Email is Invalid.'})
    def clean_OrganizationEmail(self):
        OrganizationEmail = self.cleaned_data['OrganizationEmail']
        if OrganizationEmail is None:
            raise forms.ValidationError('Email is Required.')
        elif not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', OrganizationEmail):
            raise forms.ValidationError(("Enter a valid email address."))
        return OrganizationEmail
    
    OrganizationPhone = forms.CharField(max_length=200, label='Organization Phone Number', error_messages={'required': 'Phone Number is Required .',
                                                    'invalid': 'Phone Number is Invalid.'})
    def clean_OrganizationPhone(self):
        OrganizationPhone = self.cleaned_data['OrganizationPhone']
        if OrganizationPhone is None:
            raise forms.ValidationError('Phone Number is Required.')
        elif not re.match(r'^[0-9]*$', OrganizationPhone):
            raise forms.ValidationError(("Enter a valid phone number."))
        return OrganizationPhone
    
    OrganizationAddress = forms.CharField(max_length=200, label='Organization Address', error_messages={'required': 'Organization Address is Required .',
                                                    'invalid': 'Address is Invalid.'})
    def clean_OrganizationAddress(self):
        OrganizationAddress = self.cleaned_data['OrganizationAddress']
        if OrganizationAddress is None:
            raise forms.ValidationError('Organization Address is Required.')
        elif not re.match(r'^[a-zA-Z0-9]*$', OrganizationAddress):
            raise forms.ValidationError(("Enter a valid Organization Address."))
        return OrganizationAddress
    
    Registration_Number = forms.CharField(max_length=250, label='Organization Registration Number', error_messages={'required': 'Registration Number is Required .',
                                                    'invalid': 'Registration Number is Invalid.'})
    def clean_Organization_Registration_Number(self):
        Organization_Registration_Number = self.cleaned_data['Organization_Registration_Number']
        if Organization_Registration_Number is None:
            raise forms.ValidationError('Organization Registration Number is Required.')
        elif not re.match(r'^[a-zA-Z0-9]*$', Organization_Registration_Number):
            raise forms.ValidationError(("enter a valid Organization Registration Number."))
        return Organization_Registration_Number
    
    OrganizationDigitalAddress = forms.CharField(max_length=200, label='Organization Digital Address', error_messages={'required': 'Organization Digital Address is Required .',
                                                    'invalid': 'Address is Invalid.'})
    def clean_OrganizationDigitalAddress(self):
        OrganizationDigitalAddress = self.cleaned_data['OrganizationDigitalAddress']
        if OrganizationDigitalAddress is None:
            raise forms.ValidationError('Organization Digital Address is Required.')
        return OrganizationDigitalAddress
     

    Organization_City_Of_Operation = forms.CharField(max_length=200, label='Organization City Of Operation', error_messages={'required': 'Organization City Of Operation is Required .',
                                                    'invalid': 'City Of Operation is Invalid.'})
    def clean_Organization_City_Of_Operation(self):
        Organization_City_Of_Operation = self.cleaned_data['Organization_City_Of_Operation']
        if Organization_City_Of_Operation is None:
            raise forms.ValidationError('Organization City Of Operation is Required.')
        return Organization_City_Of_Operation
    
    OrganizationStateOrRegion = forms.CharField(max_length=200, label='Organization State Or Region', error_messages={'required': 'Organization State Or Region is Required .',
                                                    'invalid': 'State Or Region is Invalid.'})
    def clean_OrganizationStateOrRegion(self):
        OrganizationStateOrRegion = self.cleaned_data['OrganizationStateOrRegion']
        if OrganizationStateOrRegion is None:
            raise forms.ValidationError('Organization State Or Region is Required.')
        return OrganizationStateOrRegion
    
    OrganizationLogo = forms.ImageField(label='Organization Logo', error_messages={'required': 'Organization Logo is Required .',
                                                    'invalid': 'Logo is Invalid.'})
    def clean_OrganizationLogo(self):
        OrganizationLogo = self.cleaned_data['OrganizationLogo']
        if OrganizationLogo is None:
            raise forms.ValidationError(' Provide at least one Organization Logo.')
        return OrganizationLogo
    
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
    






