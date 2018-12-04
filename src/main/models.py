from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Continent(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return (self.title)

class Role(models.Model):
    title = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return (self.title)

class Country(models.Model):
    title = models.CharField(max_length=255, unique=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return (self.title)

class Container(models.Model):
    title = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('N', 'Not Available'), 
        ('A', 'Available')  
    ]
    status = models.CharField(
        max_length=1, 
        choices=STATUS_CHOICES,
        default='A')

    def status_readable(self):
        return dict(Container.STATUS_CHOICES)[self.status]

    def __str__(self):
        return (self.title)


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=500, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # email = models.EmailField()
    contact = models.CharField(max_length=13)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return (self.user.first_name.title() + ' ' + self.user.last_name.title())

class Shipping(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE, blank=True)
    dept_country = models.ForeignKey(Country, related_name='dept_country', on_delete=models.CASCADE, blank=True)
    arrival_country = models.ForeignKey(Country,  related_name='arrival_country', on_delete=models.CASCADE)
    dept_date = models.DateField()
    arrival_date = models.DateField()
    send_user = models.ForeignKey(User_Profile, related_name='sending_user', on_delete=models.CASCADE, null=True)
    rec_user = models.ForeignKey(User_Profile, related_name='receiving_user', on_delete=models.CASCADE, null=True)
    SHIPPING_STATUS_CHOICES = [
        ('S', 'Shipped'),
        ('D', 'Delivered')
    ]
    shipping_status = models.CharField(
        max_length=1,
        choices=SHIPPING_STATUS_CHOICES,
        default='S')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def shipping_status_readable(self):
        return dict(Shipping.SHIPPING_STATUS_CHOICES)[self.shipping_status]

    def __str__(self):
        return (self.container.title.title() + ': ' + self.dept_country.title.title() + ' - ' + self.arrival_country.title.title())



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         User_Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()