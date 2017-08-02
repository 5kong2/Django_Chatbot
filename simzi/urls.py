from django.conf.urls import url
from django.contrib import admin
from server import views

urlpatterns = [
	url(r'keyboard/', views.keyboard),
	url(r'keyboard/', views.message),
	url(r'keyboard/', views.chat_room),
	url(r'keyboard/', views.friend),
]