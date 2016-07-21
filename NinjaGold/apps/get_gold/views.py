from django.shortcuts import render, redirect
import random, datetime

def index(request):
	#clear session variables if they exist
	if 'msg' in request.session:
		del request.session['msg']
	if 'money' in request.session:
		del request.session['money']

	return render(request, 'get_gold/index.html')

#########################################################################
def process_money(request):
	if request.method=='POST':
		#get location from session
		location=request.POST.get('location')
		#set session variable for location
		request.session['location']=location

		#check if money key is set in session; if not, initialize it
		if 'money' not in request.session:							
			request.session['money']=0
		
		#check location and and set the range of money values for that location
		if location=='farm':								
			low=10
			high=21
		elif location=='cave':
			low=5
			high=11
		elif location=='house':
			low=2
			high=6
		elif location=='casino':
			low=-50
			high=51

		#get a random number from the range set above and add it to the money session
		booty = random.randrange(low, high)					
		request.session['money'] += booty

		return redirect('/show_money')
	else:
		redirect('/')
#########################################################################
#function to format and render output to template
def show_money(request):
	#get session variables
	location = request.session['location']
	today = datetime.datetime.now().strftime('%Y/%m/%d %H:%M %p')	#get date and time
	booty = request.session['money']

	#generate activity message for gold gain/lost from each location; this dynamically creates paragraphs for the process template
	#and set text color to green for gain or red for lost
	if location != 'casino':
		msg = ('<p class="textgreen">Earned ' + str(booty) + ' golds from the '+ location + '! (' + today + ')</p>')
		textcolor='textgreen'
		msg = ('<p class="textgreen">Entered a casino and won ' + str(booty) + ' golds...Hooray! ('+ today + ')</p>')
	elif booty > 0:
		textcolor='textgreen'
	else:
		msg = ('<p class="textred">Entered a casino and lost ' + str(abs(booty)) + ' golds...Ouch... ('+ today + ')</p>')
		textcolor='textred'
	print msg

	#check if msg already exists in session; if it does not, create msg session; if it does, add msg to session
	if 'msg' not in request.session:							
		request.session['msg'] = msg 						#
	else:
		request.session['msg'] = request.session['msg'] + msg 			#

	#create context to pass back to template
	context={
		'amt': request.session['money'],
		'msg': request.session['msg']
	}

	return render(request, 'get_gold/process.html', context)
#########################################################################
#return to index page
def reset(request):
	
	return redirect('/')


