# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from item_base import *

class AuthorItem(BaseItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
	item_type = scrapy.Field()
	name = scrapy.Field()
	text_num = scrapy.Field()
	favor_num = scrapy.Field()

	def getTableSql(self):
		return "CREATE TABLE `author` (" \
			"  `name` varchar(128) NOT NULL," \
			"  `text_num` varchar(32) NOT NULL," \
			"  `favor_num` varchar(32) NOT NULL," \
			"  PRIMARY KEY (`name`)" \
			") ENGINE=InnoDB"


	def getInsertSql(self):
		return "INSERT INTO author " \
              "(name, text_num, favor_num) " \
              "VALUES (%(name)s, %(text_num)s, %(favor_num)s)"
