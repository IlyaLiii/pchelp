from django.shortcuts import render
from django.shortcuts import redirect
from .forms import FeedbackForm

from django.http import HttpResponse

def ty(request):
    return render(request , 'pchelp/ty.html')

def index(request):
	return render(request , 'pchelp/index.html')

def contact_us(request):
	form = FeedbackForm()
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("index")
			
	context = {'form':form}

	return render(request , 'pchelp/contact_us.html' , context)
