
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ticket'

urlpatterns = [
	path('', views.home, name ='home'),
	path('login/', views.login, name='login'),
	path('logout/',views.logout, name='logout'),
	path('reset_password/',views.reset_password,name = "reset_password"),
	path('reset_password_request/',views.reset_password_request,name="reset_password_request"),
	path('send_email/',views.send_email,name="send_email"),
	path('vehicle/',views.vehicle, name ='vehicle'),
	path('valet/',views.valet, name ='valet'),
	path('customer/', views.customer, name ='customer'),
	path('register/', views.register, name ='register'),
	path('request_your_car/',views.request_your_car, name = "request_your_car"),
 	path('back_vehicle/', views.back_vehicle, name ='back_vehicle'),
	path('customer_service/',views.customer_service, name ='customer_service'),
	path("vehicle_park_table/",views.vehicle_park_table,name = "vehicle_park_table"),
	path("vehicle_request_table/",views.vehicle_request_table,name="vehicle_request_table"),
	path("vehicle_all_table/",views.vehicle_all_table,name="vehicle_all_table"),
	path('vehicle_request/',views.vehicle_request, name ='vehicle_request'),
	path('request_need_help/',views.request_need_help,name="request_need_help"),
	path('change_status/',views.change_status, name='change_status'),
	path('vehicle_request_detail/',views.vehicle_request_detail, name ='vehicle_request_detail'),
	path('customer_service_error/',views.customer_service_error, name ='customer_service_error'),
	path('notification/',views.notification, name ='notification'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   