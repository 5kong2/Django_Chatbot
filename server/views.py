# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def keyboard(request):
	data = {
		"type": "buttons",
		"buttons": ["강다니엘", "옹성우", "워너원"]
	}
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")


@csrf_exempt
def message(request):
	
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	content = body['content']
	
	chat_room(request)
	
	if content == u"강다니엘":
		data = {	
			"message": {
				"text": content+" Pick!",
				"message_button": {
					"label": "WANNAONE GO!",
					"url": "http://www.wannaonego.com"
				}
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "워너원"]
			}
		}
	elif content == u"워너원":
		data = chat_room(request)
	elif content == u"옹성우":
		data = {		
			"message": {
				"text": content+" Pick!",
				"message_button": {
					"label": "WANNAONE GO!",
					"url": "http://www.wannaonego.com"
				}
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "워너원"]
			}
		}
	else:
		data = {
			"message": {
				"text" : "All I Wanna Do! " + content
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "워너원"]
			}
		}
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")

def chat_room(request):
	return	{"message":{"text" : "19961210"},"keyboard":{"type": "buttons","buttons": ["강다니엘", "옹성우", "워너원"]}}