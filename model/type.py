#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:type.py, 类型对象

from pony.orm import *
from database import d

class Type(db.Entity):
	__table__ = 'type'

