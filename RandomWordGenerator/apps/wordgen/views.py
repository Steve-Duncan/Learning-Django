from django.shortcuts import render, redirect, HttpResponse
import random, string

############################################################
#function to generate random string
def random_string(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))
############################################################
#index
def index(request):
	try:
		del request.session['attempts']
	except:
		pass

	return render(request, 'wordgen/index.html')
############################################################
#generate word
def generate_word(request):

	#validate request method
	if request.method=='POST':

		# call function to generate random string
		rand_word = random_string(14)

		#creat session for number of attempts
		if 'attempts' in request.session:
			trys = request.session['attempts']
			trys += 1
			request.session['attempts'] = trys
		else:
			request.session['attempts'] = 1
			trys=request.session['attempts']		

		#build context to return to page
		context = {
		"rand_word": rand_word,
		'attempt_num': trys
		}
		return render(request, 'wordgen/index.html', context)		
	else:
		return redirect('/')
############################################################

