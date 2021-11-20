from django.http.response import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse
import datetime

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from django.contrib import messages

import qrcode
import numpy as np
import qrcode.image.svg
from io import BytesIO

from .models import *

from tenants.utils import tenant_from_request
# Create your views here.
@csrf_exempt
def login(request):
	if request.method == 'POST': 
		tenant = tenant_from_request(request)
		if tenant.subdomain_prefix == "valet":
			ticket = request.POST.get("ticket")
			request.session["ticket_number"] = ticket

	return render(request,"login.html")

@csrf_exempt
def logout(request):
		return render(request,"login.html")

@csrf_exempt
def reset_password_request(request):

	return render(request,"main/password/password_reset.html")

@csrf_exempt
def send_email(request):

	email = request.POST.get("email")

	user = User.objects.filter(email=email).exists()

	if user:

		 return render(request,"main/password/password_reset_confirm.html",{"email":email})

	else:

		 return render(request,"login.html")


@csrf_exempt
def reset_password(request):

	password = request.POST.get("password")

	confirm_password = request.POST.get("confirm_password")

	email = request.POST.get("email")

	if password!=confirm_password:

		return render(request,"main/password/password_reset_confirm.html",{"email":email})

	else:

		user = User.objects.get(email=email)

		user.set_password(password)

		user.save()

		return render(request,"main/password/password_reset_done.html")


	
@csrf_exempt
def vehicle(request):
	if request.method == 'POST':
		
		tenant = tenant_from_request(request)
  
		name = request.POST.get('name')
		pwd = request.POST.get('pwd')

		user = authenticate(request, username=name, password=pwd)

		if user is not None:
			
			privillege = UserProfile.objects.get(user=user)

			if tenant.subdomain_prefix == "valet" and privillege.privillege.user_type=="valet":
	   
				return render(request,'qrcode.html')

			elif tenant.subdomain_prefix == "supervisor" and privillege.privillege.user_type=="supervisor":

				vehicles = VehicleTracker.objects.all()

				arrived_count = len(VehicleTracker.objects.filter(status=4))

				delayed_count = len(VehicleTracker.objects.filter(status=1))


				context = {

				'vehicles':vehicles,
				'delayed_count':delayed_count,
				'arrived_count':arrived_count,

				}

				return render(request,'vehicle_request.html',context)
			else:

				return render(request, 'login.html')

		else:
			
			return render(request, 'login.html')

	else:

		tenant = tenant_from_request(request)
  
		if tenant.subdomain_prefix == "customer":

			#the ticket number with one from the QR Code
			parked_vehicles = VehicleTracker.objects.filter(status = 6)
			phone_number = CompanyPhoneNumber.objects.all()

			context = {
				'parked_vehicles' : parked_vehicles,
				'phone_number' : phone_number
			}

			messages.success(request, 'Your Car is Parked')

			# add the part to get the ticket number from the QR Code and send 
			return render(request,"customer_service.html",context)

		return render(request,'qrcode.html')

@csrf_exempt
def valet(request):
	if request.method == "POST":
		
		tenant = tenant_from_request(request)
  
		if tenant.subdomain_prefix == "valet":
	  
			makes = VehicleMake.objects.all()
   
			ticket_number = request.POST.get("ticket")

			context = {
				'makes':makes,
				'ticket_number':ticket_number
			}

			return render(request,'vehicle.html',context)
	else:

		return render(request,'login.html' 	)

	  
@csrf_exempt
def register(request):

	if request.method == "POST":
		# get the customer's data from the post data
		card_number = request.POST.get("ticket")
		arrived_time = request.POST.get("time")
		arrived_date = request.POST.get("date")
		plate = request.POST.get('plate')
		note = request.POST.get('note')
		color= request.POST.get("color")
		model= request.POST.get("model")
		make = request.POST.get("make")

		# save the customer's data
		customer_vehicles = VehicleTracker.objects.filter(card=card_number)

		if len(customer_vehicles)==0:

			customer_vehicle = VehicleTracker.objects.create(card=card_number)
			
			customer_vehicle.time = arrived_time
			customer_vehicle.date = arrived_date
			customer_vehicle.plate = plate
			customer_vehicle.note = note
			customer_vehicle.color = color
			customer_vehicle.model = model
			customer_vehicle.make = make
			customer_vehicle.status = 6

			customer_vehicle.save()

			context = {
			 'card':card_number
			}

			return render(request,'register_success.html',context)

		else:

			return render(request,"register_fail.html")


@csrf_exempt
def request_your_car(request):

	ticket_number = request.POST.get("card")

	current_vehicle = VehicleTracker.objects.get(card = ticket_number[1:])
		
	current_status = current_vehicle.status

	if current_status == 1:
	
		return JsonResponse({"status":"Delayed"})

	elif current_status == 2:
	
		return JsonResponse({"status":"Requested"})

	elif current_status == 3:
	
		return JsonResponse({"status":"On the Way"})

	elif current_status == 4:

		time = date_time.time()

		changed_time = str(time.hour)+":"+str(time.minute)+":"+str(time.second)

		current_vehicle.time = changed_time

		current_vehicle.arrived_time = changed_time

		current_vehicle.save()
	
		return JsonResponse({"status":"Arrived"})

	elif current_status == 5:
	
		return JsonResponse({"status":"Need your help"})

	elif current_status == 6:

		current_vehicle.status = 2

		date_time = datetime.datetime.now()

		time = date_time.time()

		changed_time = str(time.hour)+":"+str(time.minute)+":"+str(time.second)

		current_vehicle.time = changed_time

		current_vehicle.requested_time = changed_time

		current_vehicle.save()

		return JsonResponse({"status":""})

	elif current_status == 7:

		return JsonResponse({"status":"Closed"})

@csrf_exempt
def change_status(request):

	card = request.POST.get("card")

	action = request.POST.get("action")

	current_vehicle = VehicleTracker.objects.get(card = card)

	if current_vehicle.status == 7:

		current_vehicle.status = action

		current_vehicle.save()

		arrived_count = len(VehicleTracker.objects.filter(status=4))

		delayed_count = len(VehicleTracker.objects.filter(status=1))

		return JsonResponse({"time": changed_time,"arrived_count":arrived_count,"delayed_count":delayed_count})


	current_vehicle.status = action

	date_time = datetime.datetime.now()

	time = date_time.time()

	changed_time = str(time.hour)+":"+str(time.minute)+":"+str(time.second)

	current_vehicle.time = changed_time

	current_vehicle.save()

	arrived_count = len(VehicleTracker.objects.filter(status=4))

	delayed_count = len(VehicleTracker.objects.filter(status=1))

	return JsonResponse({"time": changed_time,"arrived_count":arrived_count,"delayed_count":delayed_count})

@csrf_exempt
def request_need_help(request):

	card = request.POST.get("card")

	current_vehicle = VehicleTracker.objects.get(card = card)

	current_vehicle.status = 5

	current_vehicle.save()

	return JsonResponse({"success": "success"})

@csrf_exempt
def vehicle_park_table(request):

	parked_vehicles = VehicleTracker.objects.filter(status=6)

	return  HttpResponse(serializers.serialize('json', parked_vehicles), content_type="text/json-comment-filtered")

@csrf_exempt
def vehicle_request_table(request):

	requested_vehicles = VehicleTracker.objects.exclude(status=6).exclude(status=7)

	return  HttpResponse(serializers.serialize('json', requested_vehicles), content_type="text/json-comment-filtered")

@csrf_exempt
def vehicle_all_table(request):

	all_vehicles = VehicleTracker.objects.exclude(status=7)

	return  HttpResponse(serializers.serialize('json', all_vehicles), content_type="text/json-comment-filtered")

@csrf_exempt 
def back_vehicle(request):

	return render(request,'vehicle.html')


@csrf_exempt
def customer_service(request):

	return render(request,'customer_service.html')

@csrf_exempt
def vehicle_request(request):

	return render(request,'vehicle_request.html')

@csrf_exempt
def vehicle_request_detail(request):

		if request.method == 'POST':
			
			card = request.POST.get("card")

			detail_vehicle = VehicleTracker.objects.filter(card=card)
			
			return HttpResponse(serializers.serialize('json', detail_vehicle), content_type="text/json-comment-filtered")


@csrf_exempt
def customer_service_error(request):

	return render(request,'customer_service_error.html')

@csrf_exempt
def notification(request):

	return render(request,'notification.html')

@csrf_exempt
def home(request):

	tenant = tenant_from_request(request)

	if tenant.subdomain_prefix == "valet":

		return redirect("/login/")

	elif tenant.subdomain_prefix == "supervisor":

		return redirect("/login/")

	elif tenant.subdomain_prefix == "customer":

		return redirect("/vehicle/")

	elif tenant.subdomain_prefix == "admin":

		return redirect('/admin/')



@csrf_exempt
def customer(request):
	data = "http://127.0.0.1:8000/login/"
	# Name of the QR code Image file
	QRCodefile = "logincode.png"
	# instantiate QRCode object
	qrObject = qrcode.QRCode(version=1, box_size=12)
	# qrObject = qrcode.QRCode(border=10)
	# add data to the QR code
	qrObject.add_data(data)
	# compile the data into a QR code array
	qrObject.make()
	image = qrObject.make_image(fill_color="rgb(210, 175, 55)")
	image.save(QRCodefile)
	
	# print the image size (version)
	print("Size of the QR image(Version):")
	print(np.array(qrObject.get_matrix()).shape)
	return render(request,"qrcode_customer.html")
