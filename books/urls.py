from django.conf.urls import url
from books import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^books/(?P<books_id>\d+)/$',views.detail,name='detail'),
	url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)/$',views.list,name='list'),
]