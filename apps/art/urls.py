from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_registration$', views.process_registration),
    url(r'^home$', views.home),
    url(r'^process_login$', views.process_login),
    url(r'^process_add$', views.process_add),
    url(r'^logout$', views.logout),
    url(r'^delete_comment/(?P<comment_id>\d+)$', views.delete_comment),
    url(r'^show/(?P<created_by>\w+)$', views.show),
    url(r'^like_comment/(?P<comment_id>\d+)$', views.like_comment),
    url(r'^show_creator/(?P<created_by>\w+)$', views.show_creator),
    url(r'^remove_comment/(?P<comment_id>\d+)$', views.remove_comment),
    url(r'^user_profile/(?P<user_id>\d+)$', views.user_profile),
    url(r'^back$', views.back),
    url(r'^aboutme$', views.aboutme),
    url(r'^portfolio$', views.portfolio),
    url(r'^home1$', views.home1)









  ]