from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'actu'),
	url(r'^combattants/$','combattants'),
	url(r'^combattants/(?P<nom_categorie>[a-zA-Z0-9\-_]+)$','article'),
	url(r'^match/$','accueilmatch'),	
	url(r'^match/(?P<nom_categorie>[a-zA-Z0-9\-_]+)$','match'),
	url(r'^combattants/(?P<nom_categorie>[a-zA-Z0-9\-_]+)/(?P<nom_article>[a-zA-Z0-9\-_]+$)','lire'),
	url(r'^match/(?P<nom_categorie>[a-zA-Z0-9\-_]+)/(?P<id>\d+)$','combat'),
)

