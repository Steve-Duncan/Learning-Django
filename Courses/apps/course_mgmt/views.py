from django.shortcuts import render, redirect
from .models import Course

#########################################################################
#index
def index(request):
	#get all records from database
	courses=Course.objects.all()
	#build context to return to template
	context={
		'courses' : courses
	}
	return render(request, 'course_mgmt/index.html', context)
#########################################################################
#create - add a record
def create(request):
	#check request method
	if request.method == 'POST':
		#get values from input fields
		course=request.POST.get('course_name')
		description=request.POST.get('course_desc')

		#create record in database
		Course.objects.create(course_name=course, description=description)

	return redirect('/')

#########################################################################
#remove - delete record
def remove(request, id):
	#check request method
	if request.method == 'GET':
	
		#get record with id passed into function
		course = Course.objects.get(id=id)

		#build context to return to template
		context = { 
			'id' : id,
			'course': course.course_name,
			'description' : course.description
			}
		#render remove form, passing id
		return render(request, 'course_mgmt/remove.html', context)
	elif request.method == 'POST':
		#check which submit button was clicked
		if request.POST.get('keep'):
			#if keep, just return to index page
			return redirect('/')
		elif request.POST.get('delete'):
			#get the record to delete matching id passed into function
			course=Course.objects.get(id=id)
			course.delete()
		
	return redirect('/')
#########################################################################


		



