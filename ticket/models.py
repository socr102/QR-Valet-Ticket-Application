from django.db import models

from django.contrib.auth.models import User

from tenants.models import TenantAwareModel

class Usertype(models.Model):

	# uername = models.ForeignKey(User, on_delete=models.CASCADE)

	user_type = models.CharField(max_length = 100)

	def __str__(self):
		return self.user_type  

class UserProfile(models.Model): 

    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    privillege = models.ForeignKey(Usertype, on_delete=models.CASCADE)

class Customer(TenantAwareModel):

	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Valet(TenantAwareModel):

	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Supervisor(TenantAwareModel):

	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class CompanyPhoneNumber(models.Model):

	number = models.CharField(max_length = 100)

	def __str__(self):
		return self.number

class VehicleColor(models.Model):

	color = models.CharField(max_length = 100)

	def __str__(self):
		return self.color

class VehicleMake(models.Model):

	make = models.CharField(max_length = 100)

	def __str__(self):
		return self.make

class Status(models.Model):

	stauts = models.CharField(max_length = 100)

	def __str__(self):
		return self.stauts

class  VehicleTracker(models.Model):

	make = models.CharField(max_length = 100, default = "")

	card = models.CharField(max_length = 100, default = "")

	model = models.CharField(max_length = 100, default = "")

	color = models.CharField(max_length = 100, default = "")

	time = models.CharField(max_length = 100, default = "")

	date = models.CharField(max_length = 100, default = "")

	plate = models.CharField(max_length = 100, default = "")

	note = models.CharField(max_length = 100, default = "")

	requested_time = models.CharField(max_length = 100, default = "")

	arrived_time = models.CharField(max_length = 100, default = "")

	status = models.IntegerField(default = 1)


	def __str__(self):
		return self.card
