from __future__ import unicode_literals
from django.db import models

class Course(models.Model):
	course_name = models.CharField(max_length=30)
	description = models.TextField(max_length=1000)
	password = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)




