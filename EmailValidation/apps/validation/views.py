from django.shortcuts import render, redirect, HttpResponse
from .models import Email

#########################################################################
#index
def index(request):
	
	#check for message in session
	if 'msg' in request.session:
		#get the message
		msg=request.session['msg']
		#clear the message session
		del request.session['msg']
	else:
		msg=''

	#add message to context to pass to template
	context = {
		'msg' : msg
	}

	return render(request, 'validation/index.html', context)

#########################################################################
#create new record in database
def create(request):
	#get email address from form	
	email=(request.POST['email'])
	#call email validation function in the custom manager from models
	isValid = Email.userManager.validate(email)
	#get the status message
	msg=isValid[1]

	#if the email is valid...
	if isValid[0]==True:
		#add the record to the database
		Email.objects.create(email=email)
		#add the email address to the message
		msg=msg.format(email)
		#call results function, passing the message
		return results(request, msg)

	#if email is not valid...
	elif isValid[0]==False:
		#add message to session and return to index page
		request.session['msg']=msg

	return redirect('/')

#########################################################################
#delete record from database
def delete(request, id):
	#get the email object matching id passed into function
	email = Email.objects.get(id=id)
	#get the email name
	email_name = email.email
	#delete the email
	email.delete()
	#create message for deletion and pass to results function
	msg=email_name + " has been deleted!"

	return results(request, msg)

#########################################################################
#show results
def results(request, msg):
	#get all records
	emails = Email.objects.all()
	#build context to pass to results page
	context = {
		'emails' : emails,
		'msg' : msg
	}
	#show results on results page
	return render(request,'validation/results.html', context)

#########################################################################
