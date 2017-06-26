from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index, name ='my_index'),
    url(r'^register$', views.registration ,name ='my_register'),
    url(r'^login$', views.loginuser, name ='my_loginuser')]
     
