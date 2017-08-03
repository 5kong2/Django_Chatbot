# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from server.models import Member

#bottons을 string으로 변환
def content(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	content = body['content']
	return content


#첫 진입 시 보여지는 버튼
def keyboard(request):
	data = {
		"type": "buttons",
		"buttons": ["강다니엘", "옹성우", "황민현", "김재환"]
	}
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")


@csrf_exempt
def message(request):
	content_str = content(request)
	
	if content_str == u"처음으로":
		data = {
			"message": {
				"text" : "PRODUCE 101\n"+"당신의 소년을 선택해주세요!",
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "황민현", "김재환"]
			}
		}
	else:
		data = form(request)
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")


def form(request):
	content_str = content(request)
	member = Member.objects.get(name=content_str)
	
	return	{"message": {
				"text" : "You picked "+content_str+"("+member.nickname+")"+"\nRank "+ str(member.rank),
				"message_button": {
					"label": "WANNAONE GO!",
					"url": member.url
				}
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "황민현", "김재환", "처음으로"]
			}
			}