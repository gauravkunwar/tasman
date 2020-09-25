from django.contrib import admin
from tasman.models import Data, Technology, Freq

# Register your models here.
admin.site.register(Data)
admin.site.register(Technology)
admin.site.register(Freq)

admin.site.site_header = 'Tasman Administration'