# Create your views here.
#-*- coding: utf-8 -*- 

from django.shortcuts import render, get_object_or_404
from blog.models import Article
from django.http import Http404


def accueil(request):
  articles = Article.objects.all()
  return render(request,'blog/actu.html',{'derniers_articles':articles})


def view_article(request, id_article):
  text="Vous avez demandé l'article n°{0} !".format(id_article)
  return HttpResponse(text)

def lire(request, id):
 article = get_object_or_404(Article, id=id)
 return render (request, 'blog/lire.html', {'article':article})

