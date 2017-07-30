import json
import random, copy

from django.template.loader import render_to_string
from .models import *
from .gallery import Gallery
from .base import Base

class PageInterpreter():

	def __init__(self):
		self.page = {
			'mainpage': {
				'name': 'одежда для невест',
				'html': 'page_content/mainpage.html',
				'gallery_array': Gallery().build_gallery('page_content/gallery_unit.html'),
				'exclude_ids': [
					28,
					9,
					32,
				]
			}
		}

	def __build_tree_html(self, tree_elems):
		return render_to_string('page_content/tree_elems.html', {
			'tree_elems': tree_elems,	
		})

	def __build_tree_elems(self, elem, table):

		elem_id = elem.id

		field_names = Base().get_table_fields(table)

		elems = table.objects.all().values(*field_names)

		result = self.__get_all_parents(elem_id, elems, [])

		return sorted(result, key=lambda tree_elem: tree_elem['level'])

	def __get_all_parents(self, elem_id, elems, result):

		parent = [elem for elem in elems if elem['id'] == elem_id]

		if len(parent) > 0:

			result.append(parent[0])

			return self.__get_all_parents(parent[0]['parent'], elems, result)

		else:
			return result


	def build_mainpage(self, page):

		page_unit = Unit.objects.get(name=self.page[page]['name'])

		units = Unit.objects.filter(parent_id=page_unit.id).exclude(
			id__in=self.page[page]['exclude_ids'])

		result = render_to_string(self.page[page]['html'], {
			'page_head': page_unit,
			'units': units,
			'page_text': page_unit,
			'json_gallery_array': self.page['mainpage']['gallery_array']['json'],
			'gallery_array': self.page['mainpage']['gallery_array']['result'],
		})

		return result

	def build_page(self, level, unit_id):

		unit = Unit.objects.get(level=level, id=unit_id)

		tree_elems = self.__build_tree_elems(unit, Unit)

		children = Unit.objects.filter(parent_id=unit.id)

		result = render_to_string('page_content/page.html', {
			'tree_elems_html': self.__build_tree_html(tree_elems),
			'page_head': unit,
			'units': children,
			'page_text': unit,
		})

		return result