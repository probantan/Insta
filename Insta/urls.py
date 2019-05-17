from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^post/', views.post, name='post'),
    url(r'^comment/(?P<pk>\d+)', views.comment, name='comment'),
    url(r'^rest/(?P<pk>\d+)', views.rest, name='rest'),
    url(r'^like/(?P<operation>.+)/(?P<pk>\d+)', views.like, name='like'),
    url(r'^all/', views.all, name='all'),
    url(r'^search/', views.search, name='search'),
    url(r'^update/profile$', views.updateprofile, name='updateprofile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 