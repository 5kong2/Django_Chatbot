from django.conf.urls import url
from django.contrib import admin
from server import views

urlpatterns = [
	url(r'keyboard', views.keyboard),
	url(r'message', views.message),
]