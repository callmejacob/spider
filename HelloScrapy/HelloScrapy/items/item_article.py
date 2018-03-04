# -- coding: utf-8 --

import scrapy

from item_base import *

class ArticleItem(BaseItem):
	item_type = scrapy.Field()
	title = scrapy.Field()
	author = scrapy.Field()
	author_link = scrapy.Field()
	content = scrapy.Field()

	def getTableSql(self):
		return "CREATE TABLE `article` (" \
			"  `title` varchar(256) NOT NULL," \
			"  `author` varchar(128) NOT NULL," \
			"  `author_link` varchar(1024) NOT NULL," \
			"  `content` TEXT(40960) NOT NULL," \
			"  PRIMARY KEY (`title`)" \
			") ENGINE=InnoDB"


	def getInsertSql(self):
		return "INSERT INTO article " \
              "(title, author, author_link, content) " \
              "VALUES (%(title)s, %(author)s, %(author_link)s, %(content)s)"
