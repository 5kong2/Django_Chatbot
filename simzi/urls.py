from django.conf.urls import url
from django.contrib import admin
from server import views

urlpatterns = [
	url(r'keyboard', views.keyboard),
	url(r'message', views.message),
	url(r'chat_room', views.chat_room),
	url(r'friend', views.friend),
]