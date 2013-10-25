# Create your views here.
#-*- coding: utf-8 -*- 

from django.shortcuts import render

def tpl(request):
  return render(request,'comments/form.html')
