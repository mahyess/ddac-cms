from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.db import transaction

from .models import (
    Continent,
    Container,
    Country,
    Shipping,
)

from .forms import (
    UserForm, 
    ProfileForm,
    CountryForm,
    ContinentForm,
    ContainerForm,
    ShippingForm,
)

# Create your views here.
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def country(request):
    form = CountryForm()
    if request.method == 'POST':
        # form = CountryForm(request.POST, instance=request.user) ##paxi rakhnu parla.. aile pardaina
        form = CountryForm(request.POST)
        # profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your Country details was successfully updated!'))
            return redirect('main:country')
        else:
            messages.error(request, ('Please correct the error below.'))
 
    records = Country.objects.all()
        # profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/country.html', {
        'records': records,
        'form': form,
        'title': 'Add Country'
    })

def update_country(request, id):
    instance = Country.objects.get(id=id)
    form = CountryForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, ('Your Coountry details was successfully updated!'))
            return redirect('main:country')
        else:
            messages.error(request, ('Please correct the error below.'))

    records = Country.objects.all()
    context = {
        'records':records,
        'instance': instance,
        'form': form,
        'title': "Update Country Details",
        'value': 'Update Details'
    }
    return render(request, "main/country.html", context)

def continent(request):
    form = ContinentForm()
    if request.method == 'POST':
        form = ContinentForm(request.POST)
        # profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your Continent details was successfully updated!'))
            return redirect('main:continent')
        else:
            messages.error(request, ('Please correct the error below.'))

        # profile_form = ProfileForm(instance=request.user.profile)
    records = Continent.objects.all()
    return render(request, 'main/continent.html', {
        'form': form,
        'title': 'Add Continent',
        'records': records
    })

def update_continent(request, id):
    instance = Continent.objects.get(id=id)
    form = ContinentForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, ('Your Continent details was successfully updated!'))
            return redirect('main:continent')
        else:
            messages.error(request, ('Please correct the error below.'))

    # form = ContinentForm()
        # profile_form = ProfileForm(instance=request.user.profile)
    records = Continent.objects.all()
    context = {
        'records':records,
        'instance': instance,
        'form': form,
        'title': "Update Continent Details",
        'value': 'Update Details'
    }
    return render(request, "main/continent.html", context)

def container(request):
    form = ContainerForm()
    if request.method == 'POST':
        form = ContainerForm(request.POST)
        # profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your Container details was successfully updated!'))
            return redirect('main:container')
        else:
            messages.error(request, ('Please correct the error below.'))

        # profile_form = ProfileForm(instance=request.user.profile)
    records = Container.objects.all()
    status = Shipping.objects.all()
    return render(request, 'main/container.html', {
        'form': form,
        'title': 'Add Container',
        'records': records,
        'status': status
    })

def update_container(request, id):
    instance = Container.objects.get(id=id)
    form = ContainerForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, ('Your Container details was successfully updated!'))
            return redirect('main:container')
        else:
            messages.error(request, ('Please correct the error below.'))

    # form = ContainerForm()
        # profile_form = ProfileForm(instance=request.user.profile)
    records = Container.objects.all()
    status = Shipping.objects.all()
    context = {
        'records':records,
        'status': status,
        'instance': instance,
        'form': form,
        'title': "Update Container Details",
        'value': 'Update Details'
    }
    return render(request, "main/container.html", context)

def shipping_status(request):
    form = ShippingStatusForm()
    if request.method == 'POST':
        form = ShippingStatusForm(request.POST)
        # profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your Shipping Status details was successfully updated!'))
            return redirect('main:shipping-status')
        else:
            messages.error(request, ('Please correct the error below.'))

        # profile_form = ProfileForm(instance=request.user.profile)
    records = Shipping_Status.objects.all()
    return render(request, 'main/shipping_status.html', {
        'form': form,
        'title': 'Add Shipping status',
        'records': records
    })

def update_shipping_status(request, id):
    instance = Shipping_Status.objects.get(id=id)
    form = ShippingStatusForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, ('Your Shipping Status details was successfully updated!'))
            return redirect('main:shipping-status')
        else:
            messages.error(request, ('Please correct the error below.'))

    # form = Shipping_statusForm()
        # profile_form = ProfileForm(instance=request.user.profile)
    records = Shipping_Status.objects.all()
    context = {
        'records':records,
        'instance': instance,
        'form': form,
        'title': "Update Shipping Status Details",
        'value': 'Update Details'
    }
    return render(request, "main/shipping_status.html", context)

def shipping(request):
    records = Shipping.objects.all()
    return render(request, 'main/shipping.html', {
        # 'form': form,
        'title': 'Shipping List',
        'records': records
    })

def add_shipping(request, container_id):
    container = Container.objects.get(id=container_id)
    form = ShippingForm(instance=container, initial={'container': container, 'dept_country': container.country})
    if request.method == 'POST':
        form = ShippingForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.container = container
            form.dept_country = container.country
            form.save()
            messages.success(request, ('Your Shipping details was successfully updated!'))

            container.country=form.arrival_country
            container.status='N'
            container.save()

            return redirect('main:shipping')
        else:
            messages.error(request, ('Please correct the error below.'))

    # records = Shipping.objects.all()
    return render(request, 'main/ship.html', {
        'form': form,
        'title': 'Add Shipping',
        # 'records': records
    })

def update_shipping(request, id):
    instance = Shipping.objects.get(id=id)
    form = ShippingForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, ('Your Shipping details was successfully updated!'))
            return redirect('main:shipping')
        else:
            messages.error(request, ('Please correct the error below.'))

    # form = ShippingForm()
        # profile_form = ProfileForm(instance=request.user.profile)
    records = Shipping.objects.all()
    context = {
        'records':records,
        'instance': instance,
        'form': form,
        'title': "Update Shipping Details",
        'value': 'Update Details'
    }
    return render(request, "main/shipping.html", context)

def deliver(request, container_id):
    ship_instance = Shipping.objects.filter(id=container_id).latest('updated_at')
    ship_instance.shipping_status = 'D'
    ship_instance.save()

    container_instance = Container.objects.get(id=container_id)
    container_instance.status = 'A'
    container_instance.save()
    
    return redirect('main:shipping')

def index(request):
    return render(request, 'main/index.html', {'title': 'Index'})