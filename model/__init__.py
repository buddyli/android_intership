#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# from user import *
# from tables import *

# sql_debug(True)
# #创建表格并且生成映射关系
# db.generate_mapping(create_tables = True)

from mongoengine import *
from documents import *
connect('android_intership', host='172.16.22.182', port=27017)