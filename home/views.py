from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import (
    TemplateView,
)
from product.models import *

class HomeView(TemplateView):
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gaming_category = MainCategoryModel.objects.get(main_category_name="Gaming")
        context['laptops'] = Laptop.objects.order_by('?')[:1]
        nintendos = Nintendo.objects.order_by('?')[:6]
        for i in nintendos:
            print('------------',i,'------------')
        
        context['nintendos'] = Nintendo.objects.order_by('?')[:4]
        
        return context
    
    
    