from django.shortcuts import render

posts = [
	{
		'author': 'Youyou',
		'title': 'Post1',
		'content': 'First post',
		'date_posted': '29 October, 2022'
	},
	{
		'author': 'James Bond',
		'title': 'Post2',
		'content': 'Second post',
		'date_posted': '8 March, 2024'
	}
]

def home(request):
	""" render the home page of the blog """
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	""" render the about page of the blog """
	return render(request, 'blog/about.html', {'title': 'About'})