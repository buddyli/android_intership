#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from pony.orm import *
from database import db

class User(db.Entity):
	#自定义表名
	__table__ = 'my_users'

	name = Required(unicode)
	sex  = Required(unicode)
	age = Required(int)
	studio = Set('Studio')

class Studio(db.Entity):
	__table__ = 'my_studio'
	name = Required(unicode)
	user = Optional(User)

db.generate_mapping(create_tables=True)