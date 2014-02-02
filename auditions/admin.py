from django.contrib import admin
from auditions.models import Audition
from auditions.models import Company
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'url']


class AuditionAdmin(admin.ModelAdmin):
    list_display = ['company', 'time', 'city', 'state', 'url']

admin.site.register(Company, admin_class=CompanyAdmin)
admin.site.register(Audition, admin_class=AuditionAdmin)
