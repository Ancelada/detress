from django.shortcuts import render
from django.http import HttpResponse

from .base import Base

def mainpage(request):

	menubar = Base().build_menubar()

	content = None

	return render(request, 'main.html', {
		'top': {
			'menubar': menubar, 
		},
		'content': content,
	})