from django.contrib import admin
from .models import Finch, Nest, Siting, Similar, Photo

# Register your models here.
admin.site.register(Finch)
admin.site.register(Siting)
admin.site.register(Nest)
admin.site.register(Similar)
admin.site.register(Photo)
