from django.shortcuts import render

# Create your views here.


posts = [
	{
		'author': 'grazieragazzi',
		'title': 'OpenKeys writeup',
		'content': 'My first writeup ever',
		'date_posted': 'July 27, 2020'
	},
	{
		'author': 'mikasa<3',
		'title': 'Buff writeup',
		'content': 'My second writeup',
		'date_posted': 'July 28, 2020'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'GRZblog/home.html', context)

def about(request):
	return render(request, 'GRZblog/about.html', {'title': 'GRZblog'})