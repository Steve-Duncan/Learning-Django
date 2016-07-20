from django.shortcuts import render, HttpResponse
import datetime

def index(request):

	#code to get current time
	date = datetime.datetime.now().strftime('%b %d, %Y')
	time = datetime.datetime.now().strftime('%I:%M %p')
	context = {
	"date": date,
	"time": time
	}
	return render(request, 'timedisplay/page.html', context)
