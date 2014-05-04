#!/usr/bin/env python
#coding:UTF-8
#Filename: documents.py, 定义了数据库中的文档对象

from mongoengine import *
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d %H:%M:%S' # 入库格式化时间

# 菜品文档
class Menu(Document):
	id = ObjectIdField()
	name = StringField(max_length=200, required=True)
	price = StringField(max_length=50, required=True)
	addTime = DateTimeField(default=datetime.now())
	addTimeStr = StringField(default=datetime.now().strftime(DATE_FORMAT))
	# items = ListField(ReferenceField(Item)) # 一个类型可以关联多个条目
	
# 餐馆文档
class Restaurant(Document):
	id = ObjectIdField()
	name = StringField(max_length=200, required=True)
	address = StringField(max_length=200, required=False)
	telno = StringField(max_length=50, required=False)
	addTime = DateTimeField(default=datetime.now())
	addTimeStr = StringField(default=datetime.now().strftime(DATE_FORMAT))
	menu = ListField(ReferenceField(Menu))

# 内容文档。内容根据自己的类型，保存对应的条目值
class Content(Document):
	id = ObjectIdField()
	name = StringField(max_length=200, required=True)
	# typeId = LongField(required=True)
	addTime = DateTimeField(default=datetime.now())
	addTimeStr = StringField(default=datetime.now().strftime(DATE_FORMAT))
	indexed = StringField(max_length=1, required=True, default='1')
	itemValue = StringField(max_length=500)