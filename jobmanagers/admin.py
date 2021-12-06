from django.contrib import admin

# Register your models here.
from jobmanagers.models import Company,Job,Category,Location,Tech

admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Tech)