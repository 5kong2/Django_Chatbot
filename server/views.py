# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def keyboard(request):
	data = {
		"type": "buttons",
		"buttons": ["강다니엘", "옹성우"]
	}
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")


@csrf_exempt
def message(request):
	
	message = ((request.body).decode("utf-8"))
	return_json_str = json.loads(message)
	return_str = return_json_str["content"]
	
	if return_str == u"강다니엘":
		data = {	
			"message": {
				"text": "녤~",
				"photo": {
					"url": "http://post.phinf.naver.net/MjAxNzA2MThfMTQ5/MDAxNDk3NzYwMTQ3Njcx.g5Yh4qZM5d-IsFLqUJIAk2ICGdugE-QWTgk298e_-G4g.VnXqA8m4GMeMKAvQ7ACrP-K9sGJ_4hazfCev3uQA09Ag.JPEG/IibflNMZDZF3xlkrIWObOayz6FEI.jpg",
					"width": 850,
					"height": 1275
				},
				"message_button": {
					"label": "WANNAONE GO!",
					"url": "http://www.wannaonego.com"
				}
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "메인으루"]
			}
		}
	elif return_str == u"옹성우":
		data = {		
			"message": {
				"text": "옹~",
				"photo": {
					"url": "http://cafefiles.naver.net/MjAxNzA3MDJfNzcg/MDAxNDk4OTI3NjQ4OTU0.-rtgs90xqWUjg5bROJkGd2MrZiyFKDVO6WD3hj2gQtUg.a9lofCKrWC1QekHdldeeR47_iUzN0lTLXw9g-UHaHvEg.JPEG.jeonginhye06/externalFile.jpg",
					"width": 960,
					"height": 1402
				},
				"message_button": {
					"label": "WANNAONE GO!",
					"url": "http://www.wannaonego.com"
				},
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우", "메인으루"]
			}
		}
	else:
		data = {
			"message": {
				"text" : "아오"
			},
			"keyboard": {
				"type": "buttons",
				"buttons": ["강다니엘", "옹성우"]
			}
		}
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; encoding=utf-8")


def chat_room(request):
	data = {
		'message': {
			'text': 'test'
		}
	}
	
	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json; encoding=utf-8')

def friend(request):
	data = {
		'message': {
			'text': 'test'
		}
	}

	return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json; encoding=utf-8')
