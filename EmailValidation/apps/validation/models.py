from __future__ import unicode_literals
from django.db import models
import re

#regex for valid email format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
	def validate(self, email):
		#validate no blank fields
		if len(email)<1:
			return (False, 'No email entered!')
		#validate email address
		if not EMAIL_REGEX.match(email):
			#set condition to not valid
			return(False, 'Invalid email address!')
		else:
			return(True, 'The email address you entered, {}, is a VALID email address! Thank you!')

class Email(models.Model):
	email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	userManager = UserManager()
	objects = models.Manager()

