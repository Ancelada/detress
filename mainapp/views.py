from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .base import Base
from .page_interpreter import PageInterpreter

def mainpage(request):

	menubar = Base().build_menubar()
	banner = Base().build_banner()
	topbar = Base().build_topbar(request)
	bottombar = Base().build_bottombar()

	content = PageInterpreter().build_page('mainpage')

	return render(request, 'main.html', {
		'top': {
			'menubar': menubar,
			'banner': banner,
			'topbar': topbar,
		},
		'content': content,
		'bottombar': bottombar,
	})