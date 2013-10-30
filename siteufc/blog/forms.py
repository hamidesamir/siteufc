from django import forms
from blog.models import Commentaire

class CommentaireForm(forms.ModelForm):
	class Meta:
	  model = Commentaire
	  exclude = ('article')
	  
