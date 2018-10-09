from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^post/', views.post, name='post'),
    url(r'^$', views.add_profile, name='add'),
    url(r'^comment/(?P<pk>\d+)', views.comment, name='comment'),
    url(r'^others/(?P<pk>\d+)', views.others, name='others'),
    url(r'^follow/(?P<operation>.+)/(?P<pk>\d+)', views.follow, name='follow'),
    url(r'^like/(?P<operation>.+)/(?P<pk>\d+)', views.like, name='like'),
    url(r'^all/', views.all, name='all'),
    url(r'^search/', views.search_result, name='search'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)