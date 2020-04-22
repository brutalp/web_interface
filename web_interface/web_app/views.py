from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


class PagView(View):

    def get(self, request, page_id=1):
        valueList = Measurement.objects.all().order_by('id')
        page = request.GET.get('page', 1)
        paginator = Paginator(valueList, 50)
        try:
            values = paginator.page(page_id)
            values.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('pagination'))
        return render(request, 'web_app/web.html', {'values': values})


# def PagView(request):
#     valueList = Measurement.objects.all().order_by('id')
#     if request.method == 'POST':
#         pass
#         print('POST')
#         html = '<html><body>'
#         x = []
#         for key, value in request.POST.items():
#             html += f'{key}: {value}<br>'
#             x = x.append(value)
#         html += '</html></body>'
#         print(x)
#         return HttpResponse(html)
#     else:
#         print('GET')
#         page = request.GET.get('page', 1)
#         # value_on_page = request.POST.get(value)
#         # paginator = Paginator(valueList, 50)
#         # paginator = Paginator(valueList, value)
#         # paginator = Paginator(valueList, 50)
#
#         paginator = Paginator(valueList, 50)
#         try:
#             values = paginator.page(page)
#             values.num_pages_tuple = tuple(range(paginator.num_pages))
#         except:
#             return redirect(reverse('pagination'))
#         # return render(request, 'wine_app/shop.html', {'wines': wines})
#
#         # try:
#         #     values = paginator.page(page)
#         # except PageNotAnInteger:
#         #     values = paginator.page(1)
#         # except EmptyPage:
#         #     values = paginator.page(paginator.num_pages)
#         return render(request, 'web_app/web.html', {'values': values})


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
