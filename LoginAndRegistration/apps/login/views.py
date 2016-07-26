from django.shortcuts import render, redirect
from .models import User

#########################################################################
#index page
def index(request):

	return render(request, 'login/index.html')

#########################################################################
#login
def login(request):
	
	#pass request info to model login method
	loginUser=User.userManager.login(request.POST)
	#get login status message
	msg=loginUser[1]
	
	#context message to pass to show function
	context={
		'msg' : msg	
	}
	return show(request, msg)

#########################################################################
#delete user from database
def delete(request, id):
	#get the user object matching id passed into function
	user = User.objects.get(id=id)
	#get the user name
	user_name = user.first_name + ' ' + user.last_name
	#delete the user
	user.delete()
	#create message for deletion and pass to show function
	msg=user_name + " has been deleted!"
	return show(request, msg)
#########################################################################
#show results
def show(request, msg):
	#get all records
	users = User.objects.all()
	#build context to pass to results page
	context = {
		'users' : users,
		'msg' : msg
	}
	#show results on results page
	return render(request,'login/results.html', context)
#########################################################################

def create(request):
	#call model register method to create new record
	registerUser=User.userManager.register(request.POST)
	#get registration status message
	msg=registerUser[1]

	#get all records
	users = User.objects.all()

	#build context to pass to results page
	context={
		'msg' : msg,
		'users' : users
	}
	return render(request,'login/results.html', context)
