from .models import *
from django.template.loader import render_to_string
from oauth.properties import Properties

class Base():

	def __init__(self):
		pass

	def build_topbar(self, request):
		return render_to_string('top/topbar.html', {
			'vk': {
				'name' : 'VK',
				'url' : '{code_url}client_id={id}&display={display}&redirect_uri={redirect}&scope={scope}&response_type={type}&v={api}'.format(
					**Properties().vk_settings,
				)
			},
			'fb' : {
				'name' : 'FB',
				'url' : '{code_url}client_id={id}&display={display}&redirect_uri={redirect}&scope={scope}&response_type={type}'.format(
					**Properties().fb_settings,
				)
			},
			'gp' : {
				'name' : 'G+',
				'url' : '{code_url}redirect_uri={redirect}&response_type={type}&client_id={id}&scope={scope}'.format(
					**Properties().gp_settings,
				)
			},
			'ya' : {
				'name' : 'YA',
				'url' : 'https://oauth.yandex.ru/authorize?response_type={type}&client_id={id}&display={display}&force_confirm=yes&state={state}'.format(
					**Properties().ya_settings,
				)
			},
			'request': request,
		})

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

		units = Banner.objects.all().values('name', 'image', 'id')

		elems = []
		for key, value in enumerate(units):
			if key % 2 == 0:
				elems.append(render_to_string('top/banner/down.html', units[key]))
			else:
				elems.append(render_to_string('top/banner/up.html', units[key]))

		return render_to_string('top/banner/banner.html', {
			'elems': elems,
			'units': list(units),
		})

	def build_bottombar(self):
		return render_to_string('bottom/bottombar.html')