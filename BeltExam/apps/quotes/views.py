from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import User, Quote

def index(request):
	regForm = RegisterForm()
	loginForm = LoginForm()

	if 'msg' in request.session:
		#build a return string for the error message
		msg = ('<p class="err_msg">' + request.session['msg'] + '</p>')
		del request.session['msg']
	else:
		msg = ''

	context={
		'regForm' : regForm,
		'loginForm' : loginForm,
		'msg' : msg
	}
	return render(request, 'quotes/index.html', context)
#########################################################################
def addQuote(request):
	#get info from form
	author=request.POST.get('author')
	quote=request.POST.get('quote')

	#get session for user id
	user_id=request.session['user_id']
	#get the user object
	user=User.objects.get(id=user_id)
	print 'In addQuote, add quote: ' + quote
	print 'For user id: ' + str(user.id)
	#add quote to database
	newQuote=Quote.objects.create(quote=quote,author=author,user_id=user)


	return home(request)
#########################################################################

def addFave(request, id):
	#update fav status
	#get session for user id
	user_id=request.session['user_id']
	#get the user object
	user=User.objects.get(id=user_id)
	print 'In addFave, change quote status for id ' + str(id)
	Quote.objects.filter(id=id).update(favorite=True)

	return home(request)
#########################################################################
def removeFave(request, id):
	#update fav status
	#get session for user id
	user_id=request.session['user_id']
	#get the user object
	user=User.objects.get(id=user_id)
	print 'In removeFave, change quote status for id ' + str(id)
	Quote.objects.filter(id=id).update(favorite=False)

	return home(request)
#########################################################################
def showUserQuotes(request):
	user_id=request.session['user_id']
	# get the user object
	user=User.objects.get(id=user_id)

	userQuotes = user.quote_set.all()
	context={
		'user' : user,
		'quotes' : userQuotes,
	}

	return render(request, 'quotes/quotes.html', context)
#########################################################################
def home(request):
	#get session for user id
	user_id=request.session['user_id']
	#get the user object
	user=User.objects.get(id=user_id)
	print 'In home, user id: ' + str(user.id)
	print 'User alias: ' + user.alias
	quotes=Quote.objects.all()

	#create context to pass user object to template
	context={
		'user' : user,
		'quotes' : quotes
	}
	return render(request, 'quotes/home.html', context)
#########################################################################

def register(request):
	print 'Now in register, birthdate:'
	print request.POST.get('birthdate')
	if request.method=='POST':
		print 'Register request'
		print request.POST
	#pass request to register method of user class
	user=User.userManager.register(request.POST)

	if user[0]:
		#registration successful
		print 'Registration successful'
		#get the user object using returned id value
		user=User.objects.get(id=str(user[2]))
		#set session for user id
		request.session['user_id']=user.id

		return home(request)
	else:
		#registration failed
		print 'Registration failed'
		#add error message to session
		request.session['msg']=(user[1])

		return redirect('/')
#########################################################################

def login(request):
	#pass request to login method of user class
	user=User.userManager.login(request.POST)
	if user[0]:
		#login successful
		print 'Login successful'
		#get the user object using returned id value	
		user=User.objects.get(id=str(user[2]))
		#set session for user id
		request.session['user_id']=user.id
		print 'In login, add user to session: ' + str(user.id)
		return home(request)

	else:
		#login failed
		#add error message to session
		request.session['msg']=(user[1])
		
		print 'Login failed'
		print (user[1])
		return redirect('/')
#########################################################################

def logout(request):
		return redirect('/')