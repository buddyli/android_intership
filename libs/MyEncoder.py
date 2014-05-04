#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import json
from model.documents import *

class MyEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Item):
			# return [str(obj.id), obj.name, obj.indexed, obj.innerName]
			return [obj.name, obj.indexed, obj.innerName, str(obj.id)]
		else:
			return json.JSONEncoder.default(self, obj)