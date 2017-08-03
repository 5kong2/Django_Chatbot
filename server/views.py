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
	
	data = pick(request)
	
	if content == u"워너원":
		data = wannaone(request)
	elif content == u"처음으로":
		data = {
			"message": {
				"text" : "당신의 소년을 선택해주세요!",
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "워너원"]
			}
		}
	else:
		data = pick(request)
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")

def pick(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	content = body['content']
	
	return {
		"message": {
				"text" : content+" pick!",
				"message_button": {
					"label": "WANNAONE GO!",
					"url": "http://www.wannaonego.com"
				}
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "워너원", "처음으로"]
			}
	}

def wannaone(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	content = body['content']
	return	{"message": {
				"text" : "All I Wanna Do! " + content
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "워너원", "처음으로"]
			}
			}