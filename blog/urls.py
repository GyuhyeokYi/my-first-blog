from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

   	url(r'^file/$', views.file_list, name='file_list'),
   	url(r'^file/new/$', views.file_new, name='file_new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)