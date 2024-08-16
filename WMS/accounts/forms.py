# accounts/forms.py
from django import forms
from .models import CustomUser  # Import the CustomUser model

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'CompanyName_MCU',    'MCANumber_MCU',
            'GSTNumber_MCU',      'PanNumber_MCU',
            'Emailid_MCU',        'Contact_MCU',
            'Address_MCU']

class CustomUserFormWarehouse(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'WDRANumber_WCU', 'AadharNumber_WCU', 'CompanyName_WCU',
            'PanNumber_WCU', 'Emailid_WCU', 'Contact_WCU', 'Address_WCU'
          
        ]