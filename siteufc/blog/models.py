#-*- coding: utf-8 -*-
from django.db import models

class Categorie(models.Model):
	nom = models.CharField(max_length=30)

	def __unicode__(self):
	  return u"%s" % self.nom


class Article(models.Model):
	titre = models.CharField(max_length=100)
	auteur = models.CharField(max_length=42)
	image = models.CharField(max_length=30)
	contenu = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date parution")
	categorie = models.ForeignKey(Categorie) 	

	def __unicode__(self):
 	  return u"%s" % self.titre

class Match(models.Model):
	nom = models.CharField(max_length=100)
	contenu = models.TextField(null=True)
	categorie = models.ForeignKey(Categorie)
	
	def __unicode__(self):
	  return u"%s" % self.nom

class Commentaire(models.Model):
	auteur = models.CharField(max_length=30)
	contenu = models.TextField(null=True)
	article = models.ForeignKey(Article)

	def __unicode__(self):
	  return u"%s" % self.contenu

class Commentairematch(models.Model):
	auteur = models.CharField(max_length=30)
	contenu = models.TextField(null=True)
	match = models.ForeignKey(Match)

	def __unicode__(self):
	  return u"%s" % self.contenu
