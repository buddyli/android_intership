#!/usr/bin/env python
#encoding: utf-8
import json
from datetime import datetime

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入

from model.documents import *
from setting import *


@route('/user_book_history')
def user_order_history():
	mobile = request.params.get('mobile')

	orders = Order.objects(mobile=mobile)
	print orders
	json = getJsonOrders(orders)

	data = {
		'items': json
	}

	return template('views/system/user/user_book_history', data = data)

#模板中组装json实在是不方便，这里直接组装了。。。
def getJsonOrders(items):
	resList = []
	if items != None and len(items) > 0:
		for item in items:
			resDict = {
				u"name": u"%s" % item.restaurant.name,
				u"id": u"%s" % item.id,
				u"datetime": u"%s %s" % (item.orderDate, item.orderTime),
				u"cost": u"%s" % item.cost if item.cost else u'0'
			}

			if item.status == 1:
				strStatus = u'已预订'
			elif item.status == 2:
				strStatus = u'拒绝'
			elif item.status == 3:
				strStatus = u'等待'
			else:
				strStatus = u'未处理'
			resDict['status'] = strStatus

			orders = []
			for menu in item.ordered:
				orders.append(u'%s' % menu.name)
			resDict['ordered'] = orders

			resList.append(resDict)

	print json.dumps(resList)
	return json.dumps(resList)