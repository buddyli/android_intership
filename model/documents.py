#!/usr/bin/env python
#coding:UTF-8
#Filename: documents.py, 定义了数据库中的文档对象

from mongoengine import *
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d %H:%M:%S' # 入库格式化时间

	
# 餐馆文档
class Restaurant(Document):
	id = ObjectIdField()
	name = StringField(max_length=200, required=True)
	address = StringField(max_length=200, required=False)
	telno = StringField(max_length=50, required=False)
	addTime = DateTimeField(default=datetime.now())
	addTimeStr = StringField(default=datetime.now().strftime(DATE_FORMAT))
	lat = StringField(max_length=50, required=False)
	lon = StringField(max_length=50, required=False)
	price = StringField(max_length=10, required=False)
	tradeName = StringField(max_length=20, required=False, default=u'川菜')
	mStar = IntField(required=False, default=5)
	# menu = ListField(ReferenceField(Menu))

# 菜品文档--一个菜品对应一个餐馆
class Menu(Document):
	id = ObjectIdField()
	name = StringField(max_length=200, required=True)
	price = StringField(max_length=50, required=True)
	addTime = DateTimeField(default=datetime.now())
	addTimeStr = StringField(default=datetime.now().strftime(DATE_FORMAT))
	restaurant = ReferenceField(Restaurant)

# 预约订单
class Order(Document):
	id = ObjectIdField()
	mobile = StringField(max_length=11, required=True)# user's mobile
	restaurant = ReferenceField(Restaurant)# user chioced restaurant
	ordered = ListField(ReferenceField(Menu), required=False)
	orderDate = StringField(max_length=20, required=True)
	orderTime = StringField(max_length=20, required=False, default='18:00')
	#用户下单的菜品,保存这个字段是为了防止订单中的菜品被删除，导致这里查看历史记录失效。
	#为了提高响应速度，在审核预订订单时再更新orderedJson和cost两个字段
	orderedJson = StringField(max_length=500, required=False)
	cost = DecimalField(min_value=0, max_value=9999999999, precision=2, required=False, default=0)
	# 0:init, 1:accept, 2:reject, 3:queue
	status = IntField(required=False, default=0)
	addTime = DateTimeField(default=datetime.now())
	addTimeStr = StringField(default=datetime.now().strftime(DATE_FORMAT))
	num = IntField(required=False, default=1)