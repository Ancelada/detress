import json
import random, copy

from django.template.loader import render_to_string
from .models import *
from .gallery import Gallery

class PageInterpreter():

	def __init__(self):
		self.page = {
			'mainpage': {
				'name': 'одежда для невест',
				'html': 'page_content/mainpage.html',
				'gallery_array': Gallery().build_gallery('page_content/gallery_unit.html'),
			}
		}

	def build_page(self, page):

		page_unit = Unit.objects.get(name=self.page[page]['name'])

		units = Unit.objects.filter(parent_id=page_unit.id)

		result = render_to_string(self.page[page]['html'], {
			'page_head': page_unit,
			'units': units,
			'page_text': page_unit,
			'json_gallery_array': self.page['mainpage']['gallery_array']['json'],
			'gallery_array': self.page['mainpage']['gallery_array']['result'],
		})

		return result