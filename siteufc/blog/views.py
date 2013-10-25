# Create your views here.
#-*- coding: utf-8 -*- 

from django.shortcuts import render

def tpl(request):
  return render(request,'blog/tpl.html')


def view_article(request, id_article):
  text="Vous avez demandé l'article n°{0} !".format(id_article)
  return HttpResponse(text)


