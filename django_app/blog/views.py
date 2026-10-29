from django.shortcuts import render
from .models import Post

def home(request):
	""" render the home page of the blog """
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	""" render the about page of the blog """
	return render(request, 'blog/about.html', {'title': 'About'})