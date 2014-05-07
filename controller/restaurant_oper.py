#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import json
from datetime import datetime

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入

from model.documents import *
from setting import *

DATE_FORMAT = '%Y-%m-%d %H:%M:%S' # 入库格式化时间

@route('/to_add_item')
def to_add_item():
	return template('views/system/item/add', site_opt = site_opt)

@route('/add_item', method = 'POST')
def add_item():
	DATE_FORMAT = '%Y%m%d%H%M%S'
	innerName = 'attr_%s' % datetime.now().strftime(DATE_FORMAT)
	#request.params可以同时获取到GET或者POST方法传入的参数
	name = request.params.get('name')
	address = request.params.get('address')
	telno = request.params.get('telno')

	item = Restaurant(name=unicode(name, 'utf8'), address=unicode(address, 'utf8'), telno=telno)
	item.save()
	redirect('list_item')

@route('/list_item')
def list_item():
	start = request.params.get('start') or '0'
	size = request.params.get('size') or '1000'
	items = Restaurant.objects[int(start):(int(start) + int(size))]
	data = {
		'items': items
	}
	return template('views/system/item/list', data = data, site_opt = site_opt)

@route('/del_item')
def del_item():
	id = request.params.get('id')

	Restaurant.objects(id=id).delete()
	# cascade delete menus of the restaurant
	Menu.objects(restaurant=id).delete()

	redirect('/list_item')

@route('/modify_item', method = 'POST')
def modify_item():
	id = request.params.get('id')
	name = request.params.get('name')
	address = request.params.get('address')
	telno = request.params.get('telno')

	print 'modify item=====%s, %s, %s, %s' % (id, name, address, telno)
	Restaurant.objects(id=id).update(set__name = unicode(name, 'utf8'), set__address = address, set__telno = unicode(telno, 'utf-8'))
	redirect('/list_item')

@route('/to_modify_item')
def to_modify_item():
	id = request.params.get('id')
	item = Restaurant.objects(id = id)[0]
	data = {
		'item': item
	}
	return template('views/system/item/edit', data = data, site_opt = site_opt)