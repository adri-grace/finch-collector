from django.contrib import admin
from .models import Finch, Nest, Siting

# Register your models here.
admin.site.register(Finch)
admin.site.register(Siting)
admin.site.register(Nest)