# Create your views here.
#-*- coding: utf-8 -*- 

from django.shortcuts import render, get_object_or_404
from blog.models import Article, Categorie, Commentaire
from blog.forms import CommentaireForm
from django.http import Http404


def actu(request):
  categorie = Categorie.objects.all()
  return render(request,'blog/actu.html',{'toutes_categories':categorie})


def article(request, nom_categorie):
 categorie = get_object_or_404(Categorie, nom=nom_categorie) 
 article = Article.objects.filter(categorie__nom__contains=nom_categorie)
 return render (request, 'blog/article.html',{'categorie':categorie, 'tout_article':article})


def lire(request, nom_categorie, nom_article):
 
 article = Article.objects.filter(categorie__nom__contains=nom_categorie).get(titre=nom_article)
 return render (request, 'blog/lire.html', {'article':article})

