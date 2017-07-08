from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import *

class MainbarAdmin(DjangoMpttAdmin):
	pass
admin.site.register(Mainbar, MainbarAdmin)

class UnitAdmin(DjangoMpttAdmin):
	pass
admin.site.register(Unit, UnitAdmin)

class BannerAdmin(DjangoMpttAdmin):
	pass
admin.site.register(Banner, BannerAdmin)