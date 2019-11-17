from django.db import models
from locations.models import Location
from phonenumber_field.modelfields import PhoneNumberField


class Organization(models.Model):
  name = models.CharField(max_length=5000)
  short_name = models.CharField(max_length=255, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  logo = models.ImageField(blank=True, null=True)
  website = models.CharField(max_length=255, blank=True, null=True)
  email = models.EmailField(blank=True, null=True)
  location = models.ForeignKey(Location, on_delete=models.SET_NULL, related_name="organizations",  blank=True, null=True)
  contact = PhoneNumberField(blank=True, null=True)

  def __str__(self):
    if self.location:
      res = f"{ self.name }, { self.location.get_partial_location() }"
    else:
      res = f"{ self.name }"
    return res


  class Meta:
    ordering = ('name',)