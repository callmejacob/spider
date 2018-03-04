# -- coding: utf-8 --

import scrapy

from item_base import *

class ArticleDescItem(BaseItem):
	item_type = scrapy.Field()
	author = scrapy.Field()
	time = scrapy.Field()
	title = scrapy.Field()
	link = scrapy.Field()
	abstract = scrapy.Field()
	read_num = scrapy.Field()
	reply_num = scrapy.Field()
	favor_num = scrapy.Field()

	def getTableSql(self):
		return "CREATE TABLE `article_desc` (" \
			"  `title` varchar(256) NOT NULL," \
			"  `author` varchar(128) NOT NULL," \
			"  `time` varchar(128) NOT NULL," \
			"  `link` varchar(1024) NOT NULL," \
			"  `abstract` TEXT(4096) NOT NULL," \
			"  `read_num` varchar(32) NOT NULL," \
			"  `reply_num` varchar(32) NOT NULL," \
			"  `favor_num` varchar(32) NOT NULL," \
			"  PRIMARY KEY (`title`)" \
			") ENGINE=InnoDB"


	def getInsertSql(self):
		return "INSERT INTO article_desc " \
              "(title, author, time, link, abstract, read_num, reply_num, favor_num) " \
              "VALUES (%(title)s, %(author)s, %(time)s, %(link)s, %(abstract)s, %(read_num)s, %(reply_num)s, %(favor_num)s)"

