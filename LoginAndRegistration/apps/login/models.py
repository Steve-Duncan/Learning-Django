from __future__ import unicode_literals
from django.db import models
import datetime
import re, bcrypt


#regex for valid email format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

##################################################################################################
#create custom manager
class UserManager(models.Manager):
	def register(self,reg_info):
		#get values from reg_info
		first_name=reg_info['first_name']
		last_name=reg_info['last_name']
		email=reg_info['email']
		password=reg_info['password']
		confirm_pw=reg_info['confirm_pw']
		
		# #initialize message variable
		valid_status=''

		#check for any empty fields
		for field in [first_name,last_name, email, password]:
			if len(field) < 1:
				valid_status+='Empty fields are not allowed.\n'
				break
				
		#check if field contains at least 2 characters and is alpha only
		for field in [first_name,last_name]:
			if len(field)<2:
				valid_status+='Name fields must contain at least 2 characters.\n'
				break
			if not field.isalpha():
				valid_status+='Name fields must contain letters only.\n'
				break
					
		# #validate email address
		if not EMAIL_REGEX.match(email):
			valid_status+='Invalid email address\n'

		#check if password is at least 8 characters long
		if len(password)<8:
			valid_status+='Password must be at least 8 characters long\n'
		#verify passwords match
		if not confirm_pw==password:
			valid_status+="Passwords do not match!\n"

		if valid_status=='':
			print('Validation successful, ready to create')

			#hash the password with a randomly-generated salt before adding to database
			pw_encode = password.encode('utf-8')
			hashed = bcrypt.hashpw(pw_encode, bcrypt.gensalt())

			#create the record in the database
			User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
			#return message
			valid_status="Registration was successful!"
		
			return(True, valid_status)
		else:
			#validation was unsuccessful
			return(False, valid_status)
##################################################################################################
	def login(self, login_info):
		#initialize login status
		login_status=''
		#get login info from form
		email=login_info['email']
		password=login_info['password']

		#check if email found in database
		try:
			user=User.objects.get(email=email)
			user_pw=user.password

		except:
			login_status='Email not found in database'
			return(False, login_status)

		#check the password to compare with hashed value in database
		if bcrypt.hashpw(password.encode(), user_pw.encode()) == user_pw:
			#login successful
			return(True, 'Login successful!')
		else:
			#login failed
			login_status='Password may be invalid'
			return(False, login_status)
			
##################################################################################################
##################################################################################################
# create class to set up database
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name =  models.CharField(max_length=45)
	email = models.EmailField(max_length=45)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	# Connect an instance of UserManager to User model
	userManager = UserManager()
	# Re-add objects as a manager
	objects = models.Manager()

########################################################################
