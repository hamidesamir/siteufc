from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'actu'),
	url(r'^combattants/(?P<nom_categorie>[a-zA-Z0-9\-_]+)$','article'),	
	url(r'^combattants/(?P<nom_categorie>[a-zA-Z0-9\-_]+)/(?P<nom_article>[a-zA-Z0-9\-_]+$)','lire'),
)
