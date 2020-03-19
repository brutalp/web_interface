from django.shortcuts import render
from django.views import generic
from web_app.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def PagView(request):
    valueList = Measurement.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(valueList, 50)
    try:
        values = paginator.page(page)
    except PageNotAnInteger:
        values = paginator.page(1)
    except EmptyPage:
        values = paginator.page(paginator.num_pages)
    return render(request, 'web_app/web.html', {'values': values})


def PagViewTest(request):
    valueList = Measurement.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(valueList, 50)
    try:
        values = paginator.page(page)
    except PageNotAnInteger:
        values = paginator.page(1)
    except EmptyPage:
        values = paginator.page(paginator.num_pages)
    return render(request, 'web_app/webtest.html', {'values': values})


# def web_app(request):
#     return render(request, 'web_app/web.html')
#
#
# class ObjectView(generic.ListView):
#     model = Object
