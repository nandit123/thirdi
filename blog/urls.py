from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'), #replace home by post_list to make it visible and changes
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post_list/', views.post_list, name='post_list'),
]
