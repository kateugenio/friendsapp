from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^friends$', views.showDashboard),
    url(r'^user/add/(?P<id>\d+)$', views.addFriend),
    url(r'^user/(?P<id>\d+)$', views.showProfile),
    url(r'^user/(?P<id>\d+)/delete$', views.destroy),
    url(r'^logout$', views.logout),
]