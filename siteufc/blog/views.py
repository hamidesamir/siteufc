# Create your views here.
#-*- coding: utf-8 -*- 

from django.shortcuts import render, get_object_or_404
from blog.models import Article, Categorie, Commentaire, Match
from blog.forms import CommentaireForm
from django.http import Http404


def actu(request):
  categorie = Categorie.objects.all()
  match = Match.objects.all()
  return render(request,'blog/actu.html',{'toutes_categorie':categorie,'tout_match':match})


def article(request, nom_categorie):
 categorie = get_object_or_404(Categorie, nom=nom_categorie) 
 article = Article.objects.filter(categorie__nom__contains=nom_categorie)
 return render (request, 'blog/article.html',{'categorie':categorie, 'tout_article':article})

def match(request, nom_categorie):
 categorie = get_object_or_404(Categorie, nom=nom_categorie)
 match = Match.objects.filter(categorie__nom__contains=nom_categorie)
 return render (request, 'blog/match.html',{'categorie':categorie, 'tout_match':match})

def lire(request, nom_categorie, nom_article):
 article = Article.objects.filter(categorie__nom__contains=nom_categorie).get(titre=nom_article)
 commentaires = get_object_or_404(Commentaire, article=article)
 form = CommentaireForm(request.POST)
    if form.is_valid(): 
      commentaire = form.save(commit = False)
      commentaire.article = article
      commentaire.save()
 return render (request, 'blog/lire.html', {'article':article, 'tous_commentaires':commentaires, 'commentaire':commentaire})

def combat(request, nom_categorie, id):
 match = Match.objects.filter(categorie__nom__contains=nom_categorie).get(id=id)
 commentaires = get_object_or_404(Commentairematch, match=match)
 form = CommentairematchForm(request.POST)
    if form.is_valid(): 
      commentaire = form.save(commit = False)
      commentaire.match = match
      commentaire.save()
 return render (request, 'blog/combat.html', {'match':match}, 'tous_commentaires':commentaires, 'commentaire':commentaire}))

