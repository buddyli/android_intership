#!/usr/bin/env python
#coding: utf-8

class Page(object):
	"""docstring for Page"""
	def __init__(self, rc = 0, pc = 0, pn = 1, ps = 10):
		super(Page, self).__init__()
		self.rc = rc
		self.pc = pc
		self.pn = pn
		self.ps = ps
