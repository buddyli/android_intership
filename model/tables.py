#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename: item.py, 条目对象

from datetime import datetime
from pony.orm import *
from pony.converting import str2datetime#用来将字符串形式的日期转换成datetime类型的变量
from database import db

class Type(db.Entity):
	_table_ = 'tbl_type'

	id = PrimaryKey(int, auto = True, column = 'id')
	name = Required(unicode, 100, column = 'name') #使用unicode类型可以保证汉字乱码
	addTime = Optional(datetime, column = 'add_time')

class Item(db.Entity):
	_table_ = 'tbl_item'

	id = PrimaryKey(int, auto = True, column = 'id')
	name = Required(unicode, 100, column = 'name')
	innerName = Required(unicode, 100, column = 'inner_name')
	indexed = Optional(int, column = 'indexed', default = 0)
	addTime =  Optional(datetime, column = 'add_time')

class TypeItem(db.Entity):
	_table_ = 'tbl_type_item'

	id = PrimaryKey(int, auto = True, column = 'id')
	typeId = Required(int, column = 'type_id')
	itemId = Required(int, column = 'item_id')
	composite_key(typeId, itemId) # typeId and itemId are UNIQUE constraint

class Content(db.Entity):
	_table_ = 'tbl_content'

	id = PrimaryKey(int, auto = True, column = 'id')
	name  = Required(unicode, 200, column = 'name')
	typeId = Optional(int, column = 'type_id')
	# addTime = Required(datetime, column = 'add_time', sql_default = 'CURRENT_TIMESTAMP')
	# 由于sql_default编译不通过，这里需要使用str2datetime将当前时间字符串转换成datetime类型再插入表中
	addTime = Optional(datetime, column = 'add_time')
	indexed = Optional(int, column = 'indexed', default = 0)
	itemValue = Optional(unicode, 500, column = 'item_value')