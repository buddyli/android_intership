#!/usr/bin/env python
#-*- encoding:utf-8 -*-

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
# @db_session
def add_item():
	DATE_FORMAT = '%Y%m%d%H%M%S'
	innerName = 'attr_%s' % datetime.now().strftime(DATE_FORMAT)
	#request.params可以同时获取到GET或者POST方法传入的参数
	name = request.params.get('name')
	#0：索引；1：非索引
	indexed = request.params.get('indexed')
	if indexed == None:
		indexed = 1
	else:
		indexed = 0

	item = Item(name=unicode(name, 'utf8'), indexed=str(indexed), innerName=innerName)
	item.save()
	redirect('list_item')

@route('/list_item')
# @db_session
def list_item():
	start = request.params.get('start') or '0'
	size = request.params.get('size') or '1000'
	items = Item.objects[int(start):(int(start) + int(size))]
	data = {
		'items': items
	}
	return template('views/system/item/list', data = data, site_opt = site_opt)

@route('/del_item')
# @db_session
def del_item():
	id = request.params.get('id')
	# commit() # 需要手动提交删除
	Item.objects(id=id).delete()
	redirect('/list_item')

@route('/modify_item', method = 'POST')
# @db_session
def modify_item():
	id = request.params.get('id')
	name = request.params.get('name')
	#0：索引；1：非索引
	indexed = request.params.get('indexed')
	if indexed == None:
		indexed = 1
	else:
		indexed = 0

	print 'modify item=====%s, %s ,%s' % (id, name, str(indexed))
	Item.objects(id=id).update(set__name = unicode(name, 'utf8'), set__indexed = str(indexed))
	redirect('/list_item')

@route('/to_modify_item')
# @view('views/system/item/edit')
def to_modify_item():
	id = request.params.get('id')
	item = Item.objects(id = id)[0]
	data = {
		'item': item
	}
	# return dict(data = data, site_opt = site_opt)
	return template('views/system/item/edit', data = data, site_opt = site_opt)