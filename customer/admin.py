from django.contrib import admin

# Register your models here.
from .models import Bookcar,Business,Service,Car

admin.site.register(Bookcar)
admin.site.register(Service)
admin.site.register(Business)
admin.site.register(Car)