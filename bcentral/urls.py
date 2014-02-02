from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'auditions.views.index'),
    url(r'^auditions/', 'auditions.views.auditions'),
    url(r'^companies/$', 'auditions.views.companies'),
    url(r'^companies/(.+)', 'auditions.views.company_info')
)
