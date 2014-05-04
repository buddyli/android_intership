#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入

from setting import *
from model.documents import *

@route('/to_add_type_item')
@view('type_item')
def add_type_item():
	typeId = request.params.get('id')
	typeObj = Type.objects(id=typeId)[0]
	items = Item.objects();
	
	cascadeIds = []
	for item in typeObj.items:
		cascadeIds.append(item.id)

	data = {
		'type': typeObj,
		'items': items,
		'itemIds': cascadeIds
	}
	return template('views/system/type/cascade', data = data, site_opt = site_opt)

@route('/add_type_item', method = "POST")
@view('index')
def add_type_item():
	id = request.params.get('id')
	# 新的关联条目ID
	selectedItems = request.params.getall('items')
	itemList = []

	if selectedItems==None or len(selectedItems)==0:#如果取消了关联，将item清空
		pass
	else:#更新关联关系
		for itemId in selectedItems:
			itemList.append(itemId)

	Type.objects(id=id).update(set__items=itemList)

	redirect('/list_type')