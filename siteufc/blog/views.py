# Create your views here.
#-*- coding: utf-8 -*- 

from django.shortcuts import render, get_object_or_404
from blog.models import Article, Categorie, Commentaire
from blog.forms import CommentaireForm
from django.http import Http404


def accueil(request):
  categorie = Categorie.objects.all()
  return render(request,'blog/actu.html',{'toutes_categories':categorie})



def lire(request, id):
 article = get_object_or_404(Article, id=id)
 
 return render (request, 'blog/lire.html', {'article':article})


