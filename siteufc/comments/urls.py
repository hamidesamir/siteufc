from django.conf.urls import patterns, url
from django.contrib.comments.urls import urlpatterns


urlpatterns = patterns('comments.views',
	
	url(r'^post/',view='custom_comment_post',
		      name='comments-post-comment'),
	url(r'^$','form'),



)
