from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json

from config import *


class LineMessage():
	def __init__(self, messages):
		self.messages = messages
	
	def reply(self, reply_token):
		body = {
			'replyToken': reply_token,
			'messages': self.messages,
		}
		print(body)
		req = urllib.request.Request(REPLY_ENDPOINT_URL,
									 json.dumps(body).encode(),
									 HEADER
									)
		try:
			with urllib.request.urlopen(req) as res:
				body = res.read()
		except urllib.error.HTTPError as err:
			print(err)
		except urllib.error.URLError as err:
			print(err.reason)