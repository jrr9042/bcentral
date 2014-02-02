from django.shortcuts import render, render_to_response
from auditions.models import Audition, Company
from django.template import RequestContext, loader
from django.http import HttpResponse



def index(request):
    return render_to_response('index/index.html')


def maps(request):
    return render_to_response('auditions/maps/map.html')


def auditions(request):
    audition_list = Audition.objects.order_by('-time').all()
    context = RequestContext(request,
                             {'audition_list': audition_list})
    return render(request, 'auditions/auditions.html', context)


def companies(request) :
    companies_list = Company.objects.all()
    context = RequestContext(request,
                             {'company_list': companies_list})

    return render(request, 'companies/companies.html', context)


def company_info(request, company_name):
    company = Company.objects.get(name__iexact=company_name)
    audition_list = Audition.objects.filter(company=company.id)
    context = RequestContext(request,
        {'company' : company,
         'audition_list' : audition_list})
    return render(request, 'companies/company_info.html', context)