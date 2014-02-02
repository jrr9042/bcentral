from django.conf.urls import patterns, url

from auditions import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'auditions/', views.auditions, name='auditions'),
    url(r'companies/', views.companies, name='companies')
)