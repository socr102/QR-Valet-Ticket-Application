# Django-Valet-QR-Ticket

I assume that you install the python 3.9

Go to the project folder that there is  "manage.py" file:

Make the virtualenv:

	- Windows

		python -m venv venv
		.\venv\Scripts\activate

	- Linux

		1. sudo apt-get update && sudo apt-get -y upgrade

		2. sudo apt-get install python3

		3. sudo apt-get install -y python3-pip

		4. pip3 install virtualenv

		5. virtualenv env

		6. . env/bin/activate



Install the packages needed

	- Window

		pip install -r requirements.txt

	- Linux

		pip3 install -r requirements.txt

Build the table

	python3 manage.py migrate

Make the superuser

	python3 manage.py createsuperuser

Run the server 😅

	python3 manage.py runserver



The meaning of the status number in the code


	1 - Delayed
	2 - Requested
	3 - On the Way
	4 - Arrived
	5 - Need your help
	6 - Parked
	7 - Closed

This shows how to use the multi languages

	https://stackoverflow.com/questions/47940607/how-to-integrate-multi-languages-support-by-creating-language-files-in-django-2

Reference:

First command

	django-admin.py makemessages -l ar

Second command

	django-admin.py compilemessages

How to set up the environment?

I installed this project on the windows

so I am going to descirbe how to set up the envirnment on the windows 10

Please Install the Host.File.Edior

	- Windows

		https://hostsfileeditor.com/
		And then please edit like this:
		https://files.fm/u/z7u27yb5v

	- Linux

		sudo nano /etc/hosts

		please edit like this:
		
		127.0.0.1 valet.local
		127.0.0.1 supervisor.local
		127.0.0.1 customer.local




To test the valet

	http://valet.local:8000

Free account:

	username: valet
	password: Butterfly102
	email: valetmark@gmail.com 

To test the supervisor

	http://supervisor.local:8000

Free account:

	username: supervior
	password: Butterfly102
	email: supervisormark@gmail.com

To test the customer:

	http://customer.local:8000


To manage admin:

	http://admin.local:8000

You can superuser admin and password to manage the admin


Please ping me "normanburtonfree@gmail.com" if any question or need any help from me

I am very interested in Django Project

My dream become an expert with django :)😆