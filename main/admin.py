from django.contrib import admin
from .models import (
	Continent,
	Role,
	Country,
	Container,
	Shipping_Status,
	User_Profile,
	Shipping)

# Register your models here.
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Container)
admin.site.register(Role)
admin.site.register(Shipping)
admin.site.register(Shipping_Status)
admin.site.register(User_Profile)