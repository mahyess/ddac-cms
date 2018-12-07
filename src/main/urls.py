"""container URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path
from .views import (
	index, 
	update_profile,
	country,
	continent,
    container,
	update_continent,
    update_country,
    update_container,
    add_shipping,
    shipping,
    update_shipping,
    shipping_status,
    update_shipping_status,
    deliver,

)

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('country/', country, name='country'),
    # path('', include('main.views'))
    path('continent/', continent, name='continent'),
    re_path(r'^edit/continent/(?:(?P<id>[\d\-]+)/)?$', update_continent, name='update-continent'),
    re_path(r'^edit/country/(?:(?P<id>[\d\-]+)/)?$', update_country, name='update-country'),
    path('container/', container, name='container'),
    re_path(r'^edit/container/(?:(?P<id>[\d\-]+)/)?$', update_container, name='update-container'),
    path('shipping/', shipping, name='shipping'),
    re_path(r'^ship/(?:(?P<container_id>[\d\-]+)/)?$', add_shipping, name='ship'),
    re_path(r'^deliver/(?:(?P<container_id>[\d\-]+)/)?$', deliver, name='deliver'),
    # re_path(r'^deliver/(?:(?P<container_id>[\d\-]+)/)?$', deliver, name='deliver'),)
    re_path(r'^edit/shipping/(?:(?P<id>[\d\-]+)/)?$', update_shipping, name='update-shipping'),
    path('shipping-status/', shipping_status, name='shipping-status'),
    re_path(r'^edit/shipping-status/(?:(?P<id>[\d\-]+)/)?$', update_shipping_status, name='update-shipping-status'),
]
