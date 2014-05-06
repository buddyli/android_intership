#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入
from model.documents import *
from setting import *

DATE_FORMAT = '%Y-%m-%d %H:%M:%S' # 入库格式化时间

@post('/add_order', method = 'POST')
def add_item():
	#request.params可以同时获取到GET或者POST方法传入的参数
	mobile = request.params.get('mobile')
	ordered = request.params.get('ordered')
	restaurant = request.params.get('restaurant')

	save_order(mobile, ordered, restaurant)
	# typeObj = Order(mobile = mobile, ordered = ordered, restaurant = restaurant)
	return redirect('/list_order')

def save_order(mobile, ordered, restaurant):
	typeObj = Order(mobile = mobile, ordered = ordered, restaurant = restaurant)

@post('/client_add_order', method = 'POST')
def client_add_item():
	mobile = request.params.get('mobile')
	ordered = request.params.get('ordered')
	restaurant = request.params.get('restaurant')

	save_order(mobile, ordered, restaurant)
	return 'OK'

@route('/list_order')
def list_item():
	start = request.params.get('start') or '0'
	size = request.params.get('size') or '1000'
	types = Order.objects[int(start):(int(start) + int(size))]

	data = {
		'types': types
	}
	return template('views/system/order/list', data = data, site_opt = site_opt)

@route('/del_order')
def del_item():
	id = request.params.get('id')
	Order.objects(id=id).delete()
	redirect('/list_order')

@route('/modify_order')
def modify_item():
	id = request.params.get('id')
	status = request.params.get('status')

	Order.objects(id=id).update(set__status=int(status))
	redirect('/list_order')

@route('/to_modify_order')
def to_modify_item():
	id = request.params.get('id')
	item = Order.objects(id=id)[0]

	data = {
		'item': item
	}
	return template('views/system/order/edit', data = data, site_opt = site_opt)