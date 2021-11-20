# Django-Valet-QR-Ticket

I assume that you install the python 3.9

1. Go to the project folder that there is  "manage.py" file

2. Make the virtualenv 

	python -m venv venv

3. Install the packages needed

	pip install -r requirements.txt

4. Build the table

	python manage.py migrate

5. Make the superuser

	python manage.py createsuperuser

6. Run the server

	python manage.py runserver

- The meaning of the status number


	1 - Delayed
	2 - Requested
	3 - On the Way
	4 - Arrived
	5 - Need your help
	6 - Parked
	7 - Closed

- This shows how to use the multi languages

	https://stackoverflow.com/questions/47940607/how-to-integrate-multi-languages-support-by-creating-language-files-in-django-2

Reference:

1. First command

	django-admin.py makemessages -l ar

2. Second command

	django-admin.py compilemessages

How to set up the environment?

I installed this project on the windows

so I am going to descirbe how to set up the envirnment on the windows 10

1. Please Install the Host.File.Edior

	https://hostsfileeditor.com/

2. And then please edit like this:

	https://files.fm/u/z7u27yb5v

3. To test the valet

	http://valet.local:8000

Free account:

	username: valet
	password: Butterfly102
	email: valetmark@gmail.com 

4. To test the supervisor

	http://supervisor.local:8000

Free account:

	username: supervior
	password: Butterfly102
	email: supervisormark@gmail.com

5. To test the customer:

	http://customer.local:8000


6. To manage admin:

	http://admin.local:8000

You can superuser admin and password to manage the admin


Please ping me "normanburtonfree@gmail.com" if any question or need any help from me

I am very interested in Django Project

My dream become an expert with django :)