
from django.forms.models import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
# from bootstrap_datepicker_plus import DatePickerInput



class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'Source','Status', 'note']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'Status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email',
            'phone': 'Phone',
            'Source': 'Source',
            'Status': 'Status',
            'note': 'Note',
        }
        help_texts = {
            'name': 'Enter your Full Name',
            'email': 'Enter your email address',
            'phone': 'Enter your phone number',
            'Source': 'add the source of the lead',
            'Status': 'Select the status of the lead',
            'note': 'Enter any additional notes about the lead',
        }
        error_messages = {
            'name': {
                'required': 'Full name is required',
                'max_length': 'Full name is too long',
            },
            'email': {
                'required': 'Email is required',
                'invalid': 'Enter a valid email address',
            },
            'phone': {
                'required': 'Phone number is required',
                'invalid': 'Enter a valid phone number',
            },
            'Source': {
                'required': 'Source is required',
            },
            'Status': {
                'required': 'Status is required',
            },
            'note': {
                'max_length': 'Note is too long',
            },
        }


class EditLeadForm(ModelForm):  
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'Source','Status', 'note']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'Status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email',
            'phone': 'Phone',
            'Source': 'Source',
            'Status': 'Status',
            'note': 'Note',
        }
        help_texts = {
            'name': 'Enter your Full Name',
            'email': 'Enter your email address',
            'phone': 'Enter your phone number',
            'Source': 'Add the source of the lead',
            'Status': 'Select the status of the lead',
            'note': 'Enter any additional notes about the lead',
        }
        error_messages = {
            'name': {
                'required': 'Full name is required',
                'max_length': 'Full name is too long',
            },
            'email': {
                'required': 'Email is required',
                'invalid': 'Enter a valid email address',
            },
            'phone': {
                'required': 'Phone number is required',
                'invalid': 'Enter a valid phone number',
            },
            'Source': {
                'required': 'Source is required',
            },
            'Status': {
                'required': 'Status is required',
            },
            'note': {
                'max_length': 'Note is too long',
            },
        }
        

class registerForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
        }
        help_texts = {
            'username': 'Enter your username',
            'email': 'Enter your email address',
            'password': 'Enter a secure password',
        }
        error_messages = {
            'username': {
                'required': 'Username is required',
                'max_length': 'Username is too long',
            },
            'email': {
                'required': 'Email is required',
                'invalid': 'Enter a valid email address',
            },
            'password': {
                'required': 'Password is required',
                'max_length': 'Password is too long',
            },
        }