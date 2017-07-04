from .models import *
from django.template.loader import render_to_string

class Base():

	def __init__(self):
		pass


	def build_menubar(self):
		
		menubar_header_units = Mainbar.objects.filter(level=0).values('name', 'id', 'image')

		menubar_subheaders_units = Mainbar.objects.filter(
			parent_id__in=[unit['id'] for unit in menubar_header_units]
		).values('parent_id', 'name', 'id', 'image')

		result = []

		for unit in menubar_header_units:
			
			result_line = {
				'id': unit['id'],
				'name': unit['name'],
				'image': unit['image'],
				'children': [],
			}

			for child in menubar_subheaders_units:
				if child['parent_id'] == result_line['id']:
					result_line['children'].append({
						'id': child['id'],
						'name': child['name'],
					})

			result.append(result_line)

		return render_to_string('top/menubar.html', {
				'units': result,	
			})

	def build_banner(self):
		return render_to_string('top/banner.html')