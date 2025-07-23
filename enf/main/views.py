from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DeleteView
from django.http import HttpResponse
from django.template.response import TemplateResponse
from . models import Category, Product, Size
from django.db.models import Q


class IndexView(TemplateView):
  template_name = 'main/base.html'


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categories'] = Category.objects.all()
    context['current_category'] = None

    return context


  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)

    if request.headers.get('HX-Request'):
      return TemplateResponse(request, 'main/home_content.html', context)
    
    return TemplateResponse(request, self.template_name, context)


class CatalogView(TemplateView):
  template_name = 'main/base.html'

  # პროდუქტების სორტირება
  FILTER_MAPPING = {
    'color': lambda queryset, value: queryset.filter(color__iexact=value),
    'min_price': lambda queryset, value: queryset.filter(price_gte=value),
    'max_price': lambda queryset, value: queryset.filter(price_lte=value),
    'size': lambda queryset, value: queryset.filter(product_size__size__name=value),
  }


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    return 


