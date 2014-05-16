#!/usr/bin/env python
#encoding: utf-8
'''客户端相关接口'''
import json
from datetime import datetime

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入

from model.documents import *
from setting import *

#模板中组装json实在是不方便，这里直接组装了。。。
def getJsonRestaurants(items):
	resList = []
	for item in items:
		resDict = {
			u"name": u"%s" % item.name,
			u"id": u"%s" % item.id,
			u"trade_name": u"",
			u"telno": u"%s" % item.telno if item.telno else u'',
			u"address": u"%s" % item.address if item.address else u'',
			u"landmark": u"",
			u"lon": u"%s" % item.lon if item.lon else u'',
			u"lat": u"%s" % item.lat if item.lat else u'',
			u"distance": u"" ,
			u"m_star": u"",
            u"price": u"%s" % item.price if item.price else u''
		}
		resList.append(resDict)

	return json.dumps(resList)

# 单个商户详情
def getJsonDetail(item):
	if item != None:
		resDict = {
				u"name": u"%s" % item.name,
				u"id": u"%s" % item.id,
				u"trade_name": u"",
				u"telno": u"%s" % item.telno if item.telno else u'',
				u"address": u"%s" % item.address if item.address else u'',
				u"landmark": u"",
				u"lon": u"%s" % item.lon if item.lon else u'',
				u"lat": u"%s" % item.lat if item.lat else u'',
				u"distance": u"" ,
				u"m_star": u"",
	            u"price": u""
			}
	else:
		resDict = {}

	return json.dumps(resDict)

# process search restaurants requests come from clients
@route('/search_restaurants')
def search_restaurants():
	lat = request.params.get('lat')
	lon = request.params.get('lon')
	pn = request.params.get('pn') or '1'
	ps = request.params.get('ps') or '1000'

	start = (int(pn) - 1) * int(ps) 
	items = Restaurant.objects[start: start + int(ps)]

	json = getJsonRestaurants(items)
	data = {
		'items': json
	}

	return template('views/system/item/client_search', data = data)

@route('/restaurant_detail')
def restaurant_detail():
	id = request.params.get('id')

	if id != None:
		items = Restaurant.objects(id = id)[0]
		menus = Menu.objects(restaurant=id)
	else:
		items = None
		menus = []

	jsonDetail = getJsonDetail(items)
	jsonMenu = getJsonMenus(menus)

	data = {
		'items': jsonDetail,
		'menus': jsonMenu
	}
	return template('views/system/item/res_detail', data = data)

@route('/restaurant_order')
def restaurant_order():
	id = request.params.get('id')
	mobile = request.params.get('mobile')
	foods = request.params.get('foods')
	date = request.params.get('date')
	time = request.params.get('time')
	num = request.params.get('num') or '1'

	if foods == None or len(foods) <=0:
		foodsList = []
	else:
		foodsList = [item for item in foods.split(',')]

	order = Order(mobile=mobile, restaurant=id, ordered=foodsList, num=int(num), orderDate=date, orderTime=time)
	order.save()

	return template('views/system/item/order')

#模板中组装json实在是不方便，这里直接组装了。。。
def getJsonMenus(items):
	resList = []
	for item in items:
		resDict = {
			u'id': u'%s' % item.id,
			u'name': u'%s' % item.name,
			u'price': u'%s' % (item.price if item.price else '--')
		}
		resList.append(resDict)

	return json.dumps(resList)

# 获取餐馆菜单列表
@route('/restaurant_menu')
def update_menu():
	pn = request.params.get('pn') or '1'
	ps = request.params.get('ps') or '1000'
	id = request.params.get('id')

	start = (int(pn) - 1) * int(ps) 

	if id != None:
		# menus = Menu.objects(restaurant=id)[start: start + int(size)]
		menus = Menu.objects(restaurant=id)
	else:
		menus = []

	json = getJsonMenus(menus)
	data = {
		'items': json
	}

	print data
	return template('views/system/type/res_menu', data = data)

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
#返回的菜单列表中添加餐馆ID字段
def getJsonOrders(items):
	resList = []
	if items != None and len(items) > 0:
		for item in items:
			resDict = {
				u"name": u"%s" % item.restaurant.name,
				u"id": u"%s" % item.id,
				u"restaurant_id": u"%s" % item.restaurant.id,
				u"datetime": u"%s %s" % (item.orderDate, item.orderTime),
				u"num": r"%d" %(item.num if 'num' in item else 1)
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
			cost = int(0)
			for menu in item.ordered:
				orders.append(u'%s' % menu.name)
				cost += int(menu.price)

			resDict[u'ordered'] = orders
			resDict[u'cost'] = u'%d' % cost

			resList.append(resDict)

	print json.dumps(resList)
	return json.dumps(resList)