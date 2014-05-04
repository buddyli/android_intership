#!/usr/bin/env python
#coding:UTF-8
#Filename: objs.py, Mongo数据库实体

class MongoEntity(object):
	'''Mongo文档实体超类，因为类型、条目和内容都有名称、添加时间字段，因此这里定义一个超类'''
	def __init__(self, name, addTime, addTimeStr):
		self.name = name
		self.addTime = addTime
		self.addTimeStr = addTimeStr

	def name(self):
		return self.name
	def addTime(self):
		return self.addTime
	def addTimeStr(self):
		return self.addTimeStr

class Type(MongoEntity):
	def __init__(self, name, addTime, addtimeStr):
		MongoEntity.__init__(name, addTime, addTimeStr)

class Item(MongoEntity):
	def __init__(self, name, innerName, indexed, addTime, addtimeStr):
		MongoEntity.__init__(name, addTime, addTimeStr)
		self.innerName = innerName
		self.indexed = indexed

	def innerName(self):
		return self.innerName
	def indexed(self):
		return self.indexed

class Content(MongoEntity):
	def __init__(self, name, typeId, addTime, indexed, itemValue, addTimeStr):
		MongoEntity.__init__(name, addTime, addTimeStr)
		self.typeId = typeId
		self.indexed = indexed
		self.itemValue = itemValue

	def typeId(self):
		return self.typeId
	def indexed(self):
		return self.indexed
	def itemValue(self):
		return self.itemValue
