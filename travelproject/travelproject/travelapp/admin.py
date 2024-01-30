from django.contrib import admin
from .models import places
from .models import People
# Register your models here.
admin.site.register(places)
admin.site.register(People)
