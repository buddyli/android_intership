#!/usr/bin/env python
#coding:UTF-8
#Filename: documents.py, 定义了数据库中的文档对象

from mongoengine import *
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d %H:%M:%S' # 入库格式化时间

# 条目文档
class Item(Document):
	id = ObjectIdField()
	name = StringField(max_length=200, required=True)
	innerName = StringField(max_length=200, required=True)
	addTime = DateTimeField(default=datetime.now())
	addTimeStr = StringField(default=datetime.now().strftime(DATE_FORMAT))
	indexed = StringField(max_length=1, required=True, default='1')

# 类型文档。一个类型可以关联若干个条目
class Type(Document):
	id = ObjectIdField()
	name = StringField(max_length=200, required=True)
	addTime = DateTimeField(default=datetime.now())
	addTimeStr = StringField(default=datetime.now().strftime(DATE_FORMAT))
	items = ListField(ReferenceField(Item)) # 一个类型可以关联多个条目

# 内容文档。内容根据自己的类型，保存对应的条目值
class Content(Document):
	id = ObjectIdField()
	name = StringField(max_length=200, required=True)
	# typeId = LongField(required=True)
	addTime = DateTimeField(default=datetime.now())
	addTimeStr = StringField(default=datetime.now().strftime(DATE_FORMAT))
	indexed = StringField(max_length=1, required=True, default='1')
	itemValue = StringField(max_length=500)