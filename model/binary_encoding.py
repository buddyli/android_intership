#!/usr/bin/env python
#coding:UTF-8
#Filename: binary_encoding.py, 对象转储

from bson.binary import Binary

def to_binary(custom):
	return Binary(str(custom.x()), 128)

def from_binary(binary):
	return Custom(int(binary))