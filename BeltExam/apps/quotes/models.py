from __future__ import unicode_literals
from django.db import models
import datetime
# from datetime import datetime
import re, bcrypt



#regex for valid email format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


##################################################################################################

def yesterday():
	now=datetime.datetime.now()
	today=now.date()
	yesterday=datetime.date.today()-datetime.timedelta(1)
	return yesterday
##################################################################################################
#create custom manager
class UserManager(models.Manager):
	def register(self,reg_info):
		
		#get values from reg_info
		name=reg_info['name']
		alias=reg_info['alias']
		email=reg_info['email']
		password=reg_info['password']
		password_confirm=reg_info['password_confirm']
		birthdate=reg_info['birthdate']
		
		

		# #initialize message variable
		valid_status=''

		#check for any empty fields
		for field in [name, alias, email, password, birthdate]:
			if len(field) < 1:
				valid_status+='Empty fields are not allowed.\n'
				break

		
		birthdate=datetime.datetime.strptime(birthdate, '%m/%d/%Y').strftime('%Y-%m-%d')


		#check if field contains at least 2 characters and is alpha only
		if len(name)<2:
			valid_status+='Name fields must contain at least 2 characters.\n'
		# elif not name.isalpha():
		elif not all(fullname.isalpha() or fullname.isspace() for fullname in name):
			valid_status+='Name fields must contain letters only.\n'
					
		# #validate email address
		if not EMAIL_REGEX.match(email):
			valid_status+='Invalid email address\n'

		#check if password is at least 8 characters long
		if len(password)<8:
			valid_status+='Password must be at least 8 characters long\n'
		#verify passwords match
		if not password_confirm==password:
			valid_status+="Passwords do not match!\n"

		if valid_status=='':
			print('Validation successful, ready to create')

			#hash the password with a randomly-generated salt before adding to database
			pw_encode = password.encode('utf-8')
			hashed = bcrypt.hashpw(pw_encode, bcrypt.gensalt())

			#create the record in the database
			user=User.objects.create(name=name, alias=alias, email=email, password=hashed, birthdate=birthdate)	
			print 'New user created!'
			print user.id, user.name, user.email
			#return message
			valid_status="Registration was successful!"
		
			# return(True, valid_status, user)
			return (True, valid_status, user.id)
		else:
			#validation was unsuccessful
			print valid_status
			return(False, valid_status)
##################################################################################################
	def login(self, login_info):
		#initialize login status
		login_status=''
		#get login info from form
		email=login_info['email']
		password=login_info['password']

		#check for blank fields
		for field in [ email, password]:
			if len(field) < 1:
				login_status+='Empty fields are not allowed.\n'
				break
				
		#check if email found in database
		try:
			user=User.objects.get(email=email)
			user_pw=user.password

		except:
			login_status+='Email not found in database'
			return(False, login_status)

		#check the password to compare with hashed value in database
		if bcrypt.hashpw(password.encode(), user_pw.encode()) == user_pw:
			#login successful
			
			return(True, 'Login successful!', user.id, user.name)
		else:
			#login failed
			login_status+='Password may be invalid'
			return(False, login_status)
			
##################################################################################################
##################################################################################################
# create class to set up database
class User(models.Model):
	name = models.CharField(max_length=45)
	alias = models.CharField(max_length=45, null=True)
	email = models.EmailField(max_length=45)
	password = models.CharField(max_length=255)
	birthdate = models.DateField(blank=False, default=yesterday)
	#default=datetime.now									
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	# Connect an instance of UserManager to User model
	userManager = UserManager()
	# Re-add objects as a manager
	objects = models.Manager()

class Quote(models.Model):
	quote = models.CharField(max_length=255)
	author = models.CharField(max_length=45)
	user_id = models.ForeignKey(User, null=True)
	favorite = models.BooleanField(max_length=45, default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


########################################################################

