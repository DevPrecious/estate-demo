from django.shortcuts import render
from django.http import HttpResponse
from . models import House, Blog
from .forms import RequestForm
from django.contrib import messages

# Create your views here.

def home(request):
	data = House.objects.all().order_by('-id')[:3]
	context = {'data': data}
	return render(request, 'web/index.html', context)

def props(request):
	data = House.objects.all().order_by('-id')
	context = {'data': data}
	return render(request, 'web/properties.html', context)

def details(request, slug):
	form = RequestForm()

	if request.method == "POST":
		form = RequestForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thanks for your intrest, we will contact you shortly.')

	context = {'form': form}
	context["data"] = House.objects.get(url = slug)
	return render(request, 'web/details.html', context) 

def blog(request):
	data = Blog.objects.all().order_by('-id')
	context = {'data': data}
	return render(request, 'web/blog.html', context)

def blog_details(request, slug):
	context = {}
	context["data"] = Blog.objects.get(url = slug)
	return render(request, 'web/blog_details.html', context)
