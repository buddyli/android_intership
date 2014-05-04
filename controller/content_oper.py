#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入

from setting import *
from model.documents import *

@post('/add_content', method = 'POST')
def add_item():
	#request.params可以同时获取到GET或者POST方法传入的参数
	name = request.params.get('name')
	indexed = request.params.get('indexed') or None
	itemValue = request.params.get('itemValues')

	if indexed == None:
		indexed = '1'
	else:
		indexed = '0'

	typeObj = Content(name = unicode(name, 'utf8'), addTime = datetime.now(), indexed = str(indexed), itemValue = unicode(itemValue, 'utf8'))
	typeObj.save()
	redirect('/list_content')

@route('/list_content')
def list_item():
	start = request.params.get('start') or '0'
	size = request.params.get('size') or '1000'
	items = Content.objects()[int(start):(int(start) + int(size))]

	data = {
		'items': items
	}
	return template('views/system/content/list',data = data, site_opt = site_opt)

@route('/del_content')
def del_item():
	id = request.params.get('id')
	Content.objects(id=id).delete()
	redirect('/list_content')

@route('/modify_content', method = 'POST')
def modify_item():
	id = request.params.get('id')
	name = request.params.get('name')
	indexed = request.params.get('indexed') or None

	if indexed == None:
		indexed = '1'
	else:
		indexed = '0'

	Content.objects(id=id).update(set__name=unicode(name, 'utf8'),set__indexed = indexed)
	redirect('/list_content')

@route('/to_modify_content')
def to_modify_item():
	id = request.params.get('id')
	item = Content.objects(id=id)[0]

	data = {
		'item': item
	}
	return template('views/system/content/edit', data = data, site_opt = site_opt)

# 跳转到添加内容，级联加载类型及其对应的条目
@route('/to_add_content')
def to_add_content():
	types = Type.objects()
	return template('views/system/content/add',data = types, site_opt = site_opt)

@route('/selectItems', method = 'POST')
def selectItems():
	import json
	from libs.MyEncoder import MyEncoder

	typeId = request.params.get('typeId')

	typeObj = Type.objects(id=typeId)[0]
	itemList = []
	items = []
	for item in typeObj.items:
		items.append(Item.objects(id=item.id)[0])

	for tmpItem in items:
		itemList.append(MyEncoder().default(tmpItem))

	response.content_type = 'application/json'
	print json.dumps(itemList)
	return json.dumps(itemList)
