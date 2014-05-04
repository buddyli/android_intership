#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename: db_oper.py, 数据相关操作

# from pony.orm import *
from datetime import datetime
# from pony.converting import str2datetime#用来将字符串形式的日期转换成datetime类型的变量
# from model.tables import *

#保存条目
def save_item(name, indexed = 0):
	dt = datetime.now()
	print name, indexed, dt
	# item = Item(name = unicode(name, 'utf8'), indexed = int(indexed), addTime = dt)
	# commit()

#条目列表
def list_item(start, size):
	pass

#删除条目
def del_item(id):
	pass

#加载单条条目
def get_one_item(id):
	pass