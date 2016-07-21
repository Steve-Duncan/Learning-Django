from django.shortcuts import render, redirect, HttpResponse

def index(request):
	#set message for display on initial page; set context for return to index page
	msg="No ninjas here"
	context={
		'msg': msg
	}
	return render(request, 'ninja/index.html', context)

def ninja(request, color=None):
	
	# set path for images to return depending on parameter passed from url
		
	if color==None:
		turtle='ninja/images/TMNT.jpg'
	elif color=="red":
		turtle='ninja/images/raphael.jpg'
	elif color=="blue":
		turtle='ninja/images/leonardo.jpg'
	elif color=="purple":
		turtle='ninja/images/donatello.jpg'
	elif color=="orange":
		turtle='ninja/images/michelangelo.jpg'
	else:
		turtle='ninja/images/notapril.jpg'


	context={
		'turtle': turtle
	}
	return render(request, 'ninja/index.html', context)


