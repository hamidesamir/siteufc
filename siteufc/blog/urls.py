from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'accueil'),
	url(r'^article/(?P<id>\d+)$','lire'),	
)
