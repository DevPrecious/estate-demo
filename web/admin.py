from django.contrib import admin
from .models import House, Blog, Requests 

# Register your models here.

admin.site.register(House)
admin.site.register(Blog)
admin.site.register(Requests)
