from django.template.loader import render_to_string
from .models import *

class PageInterpreter():

	def __init__(self):
		self.page = {
			'mainpage': {
				'name': 'одежда для невест',
				'html': 'page_content/mainpage.html',
			}
		}

	def build_page(self, page):

		page_head = Unit.objects.get(name=self.page[page]['name'])

		units = Unit.objects.filter(parent_id=page_head.id)

		result = render_to_string(self.page[page]['html'], {
			'page_head': page_head,
			'units': units,
		})

		return result