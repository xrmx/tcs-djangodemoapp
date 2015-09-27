from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.new_todo, name="new_todo"),
    url(r'^(?P<todo_id>\d+)$', views.detail, name="detail"),
    url(r'^(?P<todo_id>\d+)/item/add$', views.add_item, name="add_item"),
    url(r'^(?P<todo_id>\d+)/item/(?P<item_id>\d+)/remove$', views.remove_item, name="remove_item"),
]
