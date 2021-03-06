#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import json
from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入
from model.documents import *
from setting import *

DATE_FORMAT = '%Y-%m-%d %H:%M:%S' # 入库格式化时间

@get('/to_add_type')
def to_add_type():
	restaurants = Restaurant.objects()
	return template('views/system/type/add', data = restaurants, site_opt = site_opt)

@post('/add_type', method = 'POST')
def add_item():
	#request.params可以同时获取到GET或者POST方法传入的参数
	name = request.params.get('name')
	price = request.params.get('price')
	restaurant = request.params.get('restaurant')

	typeObj = Menu(name = unicode(name, 'utf8'), price = price, restaurant = restaurant)
	typeObj.save()
	return redirect('/list_type')

@route('/list_type')
def list_item():
	start = request.params.get('start') or '0'
	size = request.params.get('size') or '1000'
	types = Menu.objects[int(start):(int(start) + int(size))]

	data = {
		'types': types
	}
	return template('views/system/type/list', data = data, site_opt = site_opt)

@route('/del_type')
def del_item():
	id = request.params.get('id')
	Menu.objects(id=id).delete()
	redirect('/list_type')

@route('/modify_type', method = 'POST')
def modify_item():
	id = request.params.get('id')
	name = request.params.get('name')
	price = request.params.get('price')
	Menu.objects(id=id).update(set__name=unicode(name, 'utf8'), set__price=price)
	redirect('/list_type')

@route('/to_modify_type')
def to_modify_item():
	id = request.params.get('id')
	item = Menu.objects(id=id)[0]

	data = {
		'item': item
	}
	return template('views/system/type/edit', data = data, site_opt = site_opt)