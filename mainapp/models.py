from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Mainbar(MPTTModel):
	name = models.CharField(max_length=400)
	description = models.TextField(null=True, blank=True)
	short_description = models.TextField(null=True, blank=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
	image = models.ImageField(blank=True, null=True)
	cost = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.name

class Unit(MPTTModel):
	name = models.CharField(max_length=400)
	description = models.TextField(null=True, blank=True)
	short_description = models.TextField(null=True, blank=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
	image = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.name

class Banner(MPTTModel):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='banner', blank=True, null=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

	def __str__(self):
		return self.name