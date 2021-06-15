from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'website/homepage.html')
 
 
def aktu(request):
 	return render(request, 'website/aktu.html')

def siet(request):
	return render(request, 'website/siet.html')

def contact(request):
	return render(request, 'website/contact.html')

def course(request):
	return render(request, 'website/course.html')

def admission(request):
	return render(request, 'website/admission.html')

def fees(request):
	return render(request, 'website/fees.html')

def circular(request):
	return render(request, 'website/circular.html')


def syllabus(request):
	return render(request, 'website/syllabus.html')

def complainbox(request):
	return render(request, 'website/complainbox.html')







