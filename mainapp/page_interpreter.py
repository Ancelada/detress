from django.template.loader import render_to_string
from .models import *

class PageInterpreter():

	def __init__(self):
		self.page = {
			'mainpage': {
				'name': 'одежда для невест',
				'html': 'page_content/mainpage.html',
				'gallery': self.__build_gallery(),
			}
		}

	def build_page(self, page):

		page_unit = Unit.objects.get(name=self.page[page]['name'])

		units = Unit.objects.filter(parent_id=page_unit.id)

		result = render_to_string(self.page[page]['html'], {
			'page_head': page_unit,
			'units': units,
			'page_text': page_unit,
		})

		return result

	def __build_gallery(self):
		
		result = []

		return result