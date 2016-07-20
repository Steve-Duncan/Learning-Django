from django.shortcuts import render, redirect, HttpResponse

############################################################
#index
def index(request):
	# del request.session['submits']	#uncomment to clear session
	return render(request,'dojosurvey/index.html')

############################################################
#process
def process(request):
	
	print request.method
	#get field values from form
	if request.method == 'POST':

		#creat session variable for number of attempts
		if 'submits' in request.session:
			submits = request.session['submits']
			submits += 1
			request.session['submits'] = submits
		else:
			request.session['submits'] = 1

		#create session variables for input data from form
		request.session['name'] = request.POST.get('name')
		request.session['location'] = request.POST.get('location')
		request.session['language'] = request.POST.get('language')
		request.session['comment'] = request.POST.get('comment')
		#call result function
		return redirect('/result')
	else:
		return redirect('/')

############################################################
#result
def result(request):
	#build context for return
	context = {
		"name": request.session['name'],
		'location': request.session['location'],
		'language': request.session['language'],
		'comment': request.session['comment'],
		'submits': request.session['submits']
		}
	return render(request, 'dojosurvey/result.html', context)

