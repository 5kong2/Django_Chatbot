# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def keyboard(request):
	data = {
		"type": "buttons",
		"buttons": ["제발좀", "돼라ㅅㅂ"]
	}

	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")


@csrf_exempt
def message(request):
	data = {
		"message": {
			"text": "을 선택하셨습니다."
		},		
		"keyboard": {
			"type": "buttons",
			"buttons": ["이전으로 돌아가기"]
		}
	}
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")
