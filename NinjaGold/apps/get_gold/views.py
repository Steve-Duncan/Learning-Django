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
#calculate how much gold earned from each location; location is passed from form
#as route parameter
def process_money(request, location):
	if request.method=='POST':
		
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
		else:
			redirect('/')

		#get a random number from the range set above and add it to the money session
		booty = random.randrange(low, high)
		#booty is the amount earned each visit
		request.session['booty'] = booty
		#money is the total amount earned
		request.session['money'] += booty

		#call function to display the results
		return redirect('/show_money')
	else:
		redirect('/')
#########################################################################
#function to format and render output to template
def show_money(request):
	#get session variables
	location = request.session['location']
	booty = request.session['booty']

	#get today's date and time
	today = datetime.datetime.now().strftime('%Y/%m/%d %H:%M %p')	#get date and time

	#generate activity message for gold gain/lost from each location; this dynamically creates paragraphs for the process template
	#and set text color to green for gain or red for lost
	if location != 'casino':
		msg = ('<p class="textgreen">Earned ' + str(booty) + ' golds from the '+ location + '! (' + today + ')</p>')
		textcolor='textgreen'	
	elif booty > 0:
		msg = ('<p class="textgreen">Entered a casino and won ' + str(booty) + ' golds...Hooray! ('+ today + ')</p>')
		textcolor='textgreen'
	else:
		msg = ('<p class="textred">Entered a casino and lost ' + str(abs(booty)) + ' golds...Ouch... ('+ today + ')</p>')
		textcolor='textred'

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
# def reset(request):
# 	if 'msg' in request.session:
# 		del request.session['msg']
# 	if 'money' in request.session:
# 		del request.session['money']
# 	return render(request, 'get_gold/index.html')


