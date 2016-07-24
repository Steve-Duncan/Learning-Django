from django.shortcuts import render, redirect
from .models import Course, Comment

#########################################################################
#index- display initial page, showing all current courses
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
	#return to initial page
	return redirect('/')

#########################################################################
#remove - delete record
def remove(request, id):
	#check request method
	if request.method == 'GET':
		#get record for id passed into function
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
			#if delete button was clicked,
			#get the record to delete matching id passed into function
			course=Course.objects.get(id=id)
			#delete the record
			course.delete()
	#return to initial page
	return redirect('/')
#########################################################################
#show comments for a given course
def show_comment(request, id):
	#get record for id passed into function
	course = Course.objects.get(id=id)
	#build context to return to template
	context = { 
	'id' : id,
	'course': course.course_name,
	'description' : course.description,
	'course' : course
	}
	return render(request,'course_mgmt/comments.html', context)
#########################################################################
#add comment to a record
def add_comment(request, id):
	#check which submit button was clicked
	#if the comment button was clicked:
	if request.POST.get('comment'):
		#get record for id passed into function
		course = Course.objects.get(id=id)
		#get values from input fields
		comment=request.POST.get('comment_text')
		#create record in database
		Comment.objects.create(comment=comment, course=course)
		# return to show comments page
		return show_comment(request, id)

	#if no comment button was clicked
	elif request.POST.get('no_comment'):
		#just return to index page	
		return redirect('/')
#########################################################################
#delete a comment
def delete_comment(request, id):
	#get the comment for id passed into function
	comment = Comment.objects.get(id=id)
	#get the related course id
	course_id = comment.course.id
	#delete the comment
	comment.delete()
	
	# return to show comment page
	return show_comment(request, course_id)
		


