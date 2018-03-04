# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from items import *

'''
class HelloscrapyPipeline(object):

	def open_spider(self, spider):
   		self.file = open('./items.txt', 'w')

	def close_spider(self, spider):
   		self.file.close()

	def process_item(self, item, spider):
		line = json.dumps(dict(item))
		self.file.write(line)
		return item
'''

import mysql.connector
from db import *

class MySqlPipeline(object):

	def __init__(self):
		self.mysqldb = MySqlDb('jianshu')
		pass

	def open_spider(self, spider):
		self.mysqldb.open()

	def close_spider(self, spider):
		self.mysqldb.close()

	def process_item(self, item, spider):
		# print '$' * 50
		# print item['item_type']
		item.insertToDb(self.mysqldb)
		# print '$' * 50
