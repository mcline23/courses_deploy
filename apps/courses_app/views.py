from django.shortcuts import render, redirect
from .models import Course


def index (request):

	context= {
		"courses": Course.objects.all()
		}
	#courses = Course.objects.all()
	#print courses
	return render(request, 'courses_app/index.html', context)

def addcourse(request):

	Course.objects.create(name=request.POST['title'], description=request.POST['sort'])
	return redirect('/')

def delete(request, id):
	context= {
			"courses": Course.objects.all()
		}
	return render(request, 'courses_app/delete.html')




	#if request.method =='POST':

		#name = request.POST['course']
		#Course.object.create(
		#description = request.POST['text']
		#query = Course(name = name, description = text)
		#query.save()
		#Course.object.create(description) = request.POST['description']
		#print name
		#print description
		#return redirect('/')


