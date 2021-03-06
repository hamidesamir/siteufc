# Create your views here.
#-*- coding: utf-8 -*- 

from django.shortcuts import render, get_object_or_404
from blog.models import Article, Categorie, Commentaire, Match, Commentairematch
from blog.forms import CommentaireForm, CommentairematchForm
from django.http import Http404


def actu(request):
  categorie = Categorie.objects.all()
  match = Match.objects.all()
  return render(request,'blog/actu.html',{'toutes_categorie':categorie,'tout_match':match})

def combattants(request):
  categorie = Categorie.objects.all()
  return render(request,'blog/accueilcombattants.html', {'toutes_categories':categorie})

def accueilmatch(request):
  match = Match.objects.all()
  return render(request,'blog/accueilmatch.html',{'tout_match':match})

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
 commentaires = Commentaire.objects.filter(article__titre__contains=nom_article)
 if request.method == 'POST':
  form = CommentaireForm(request.POST,instance=Commentaire()) 
  if form.is_valid(): 
	commentaire = form.save(commit=False)
	commentaire.article = article
	commentaire.save()
 else:
	form=CommentaireForm()
 return render (request, 'blog/lire.html', {'article':article, 'tous_commentaires':commentaires, 'form':form})

def combat(request, nom_categorie, id):
 match = Match.objects.filter(categorie__nom__contains=nom_categorie).get(id=id)
 commentaires = Commentairematch.objects.filter(match__id__contains=id)
 if request.method == 'POST':
  form = CommentairematchForm(request.POST,instance=Commentairematch()) 
  if form.is_valid(): 
	commentairematch = form.save(commit=False)
	commentairematch.match = match
	commentairematch.save()
 else:
	form=CommentairematchForm()
 return render (request, 'blog/combat.html', {'match':match, 'tous_commentaires':commentaires,'form':form})

