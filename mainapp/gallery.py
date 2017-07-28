import json
from .models import Gallery as G
from django.template.loader import render_to_string

class Gallery():

	def build_gallery(self, template):

		result = []

		girls = G.objects.filter(level=0).order_by('?').values(
			'id',
			'name',
			'Unit__name',
			'image',
			'image_small',
			'parent_id',
		)

		photoes = G.objects.filter(
			parent_id__in=[girl['id'] for girl in girls]
		).order_by('?')

		for girl in girls:

			result_line = {
				'gallery_id': girl['id'],
				'name': girl['name'],
				'unit_name': girl['Unit__name'],
				'photoes': [],
			}

			for photo in photoes:

				if photo.parent_id == girl['id']:
					
					result_line['photoes'].append({
						'gallery_id': photo.id,
						'html': render_to_string(template, {
							'parent_id': girl['id'],
							'gallery_id': photo.id,
							'girl_name': girl['name'],
							'unit_name': girl['Unit__name'],
							'image': photo.image,
							'image_small': photo.image_small,	
						})
					})

			result.append(result_line)

		return {
			'json': json.dumps(result[:12]),
			'result': result[:12],
		}