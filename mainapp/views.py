from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .base import Base
from .page_interpreter import PageInterpreter

def mainpage(request):

	menubar = Base().build_menubar()
	banner = Base().build_banner()

	content = PageInterpreter().build_page('mainpage')

	return render(request, 'main.html', {
		'top': {
			'menubar': menubar,
			'banner': banner,
		},
		'content': content,
	})