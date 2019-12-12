from django.db import models

class Country(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)

  class Meta:
    verbose_name_plural = "Countries"

  def __str__(self):
    return f"{ self.name }"

  def get_country(self):
    return self.__str__()


class State(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")

  class Meta:
    verbose_name_plural = "States"

  def __str__(self):
    return f"{ self.name }, { self.country.name }"

  def get_state(self):
    return self.__str__()


class City(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")

  class Meta:
    verbose_name_plural = "Cities"

  def __str__(self):
    return f"{ self.name}, { self.state.name}, { self.state.country.name }"
  
  def get_city(self):
    return self.__str__()


class Location(models.Model):
  street = models.CharField(max_length=255)
  address1 = models.CharField(max_length=255, blank=True, null=True)
  address2 = models.CharField(max_length=255, blank=True, null=True)
  landmark = models.CharField(max_length=255, blank=True, null=True)  
  pincode = models.IntegerField()
  city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="locations")
  
  def get_partial_location(self):
    location = ""
    for i in [self.city.name, self.city.state.name, self.city.state.country.name]:
      if i is not None:
        location = location + ', ' + i
    location = location.strip(', ')
    return location

  def __str__(self):
    location = ""
    for i in [self.street, self.address1, self.address2, self.city.name, self.city.state.name, self.city.state.country.name]:
      if i is not None:
        location = location + ', ' + i
    location = location.strip(', ')
    return location

  def get_location(self):
    return self.__str__()

  def get_country(self):
    return str(self.city.state.country.name)

  def get_state(self):
    return str(self.city.state.name)

  def get_city(self):
    return str(self.city.name)

