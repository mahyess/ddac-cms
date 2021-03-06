from django import forms

from django.contrib.auth.models import User
from .models import (
    User_Profile, 
    Continent,
    Country, 
    Container, 
    Shipping,
    Shipping_Status,

)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email'
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
            'country', 
            'role',
            'contact'
        ]

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            'title', 
            'continent'
        ]

class ContinentForm(forms.ModelForm):
    class Meta:
        model = Continent
        fields = [
            'title', 
        ]

class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = [
            'title', 
            'country'
        ]

class ShippingStatusForm(forms.ModelForm):
    class Meta:
        model = Shipping_Status
        fields = [
            'title', 
        ]

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = [
            'container', 
            'dept_country',
            'arrival_country',
            'dept_date',
            'arrival_date',
            'shipping_status'
        ]
    def __init__(self, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['container'].widget.attrs['readonly'] = True
            self.fields['dept_country'].widget.attrs['readonly'] = True