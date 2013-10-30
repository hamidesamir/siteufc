from django import forms
from blog.models import Commentaire, Commentairematch

class CommentaireForm(forms.ModelForm):
	class Meta:
	  model = Commentaire
	  exclude = ('article')
	  
class CommentairematchForm(forms.ModelForm):
	class Meta:
	  model = Commentairematch
	  exclude = 'match'
