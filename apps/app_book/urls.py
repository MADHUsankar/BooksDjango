from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^homepage$', views.homepage , name ='home_page') ,
    url(r'^addbook$', views.addbook , name ='add_book') ,
    url(r'^showbook/(?P<id>\d+)$', views.showbook , name ='show_book') ,
    url(r'^showuser/(?P<id>\d+)$', views.showuser , name ='show_user') ,
    url(r'^deletereview/(?P<id>\d+)$', views.deletereview , name ='delete_review') ,
    url(r'^logout$', views.logout , name ='logout') 
    ]
     