from django import forms
from blog.models import Commentaire

class CommentaireForm(forms.ModelForm):
	class Meta:
	  model = Commentaire
	  exclude = ('article')
	  
<<<<<<< HEAD
=======
class CommentairematchForm(forms.ModelForm):
	class Meta:
	  model = Commentairematch
	  exclude = ('match')
>>>>>>> cf3f9af8b4f2e7a2cdda22cdad0304538bd39eb1
