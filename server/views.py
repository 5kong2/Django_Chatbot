# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from server.models import Member

# Create your views here.
def keyboard(request):
	data = {
		"type": "buttons",
		"buttons": ["강다니엘", "옹성우", "워너원"]
	}
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")

@csrf_exempt
def message(request):
	str = content(request)
	
	if str == u"워너원":
		data = wannaone(request)
	elif str == u"처음으로":
		data = {
			"message": {
				"text" : "PRODUCE 101\n"+"당신의 소년을 선택해주세요!",
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "워너원"]
			}
		}
	else:
		data = wannaone(request)
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")


def content(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	content = body['content']
	return content


def wannaone(request):
	str = content(request)
	if str == u"워너원":
		add_str = "All I Wanna Do! "
	else:
		#add_str = "You picked "
		if str == Member.objects.get(name="강다니엘").name:
			add_str = "실행이 잘 되었습니다. "
		else:
			add_str = "You picked "
		
	return	{"message": {
				"text" : add_str + str,
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