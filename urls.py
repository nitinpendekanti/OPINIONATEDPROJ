from django.conf.urls import url
from . import views

app_name = 'politics'

urlpatterns = [
    #/politics/
    url(r'^$', views.IndexView.as_view(), name ='index'),
    
    #/politics/debate id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    
    url(r'debate/add/$', views.DebateCreate.as_view(), name = 'debate-add'),
    url(r'(?P<pk>[0-9]+)/comment/$', views.CommentCreate.as_view(), name = 'comment-add'),
    url(r'(?P<pk>[0-9]+)/reply/$', views.ReplyCreate.as_view(), name = 'reply-add'),
   
 


]