# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from item_base import *

class AuthorItem(BaseItem):
	item_type = scrapy.Field()
	user_name = scrapy.Field()
	user_link = scrapy.Field()
	head_url = scrapy.Field()
	mail_link = scrapy.Field()
	follow_num = scrapy.Field()
	follower_num = scrapy.Field()
	page_num = scrapy.Field()
	words_num = scrapy.Field()
	favored_num = scrapy.Field()


	def getTableSql(self):
		return "CREATE TABLE `author` (" \
			"  `user_name` varchar(128) NOT NULL," \
			"  `user_link` varchar(1024) NOT NULL," \
			"  `head_url` varchar(1024) NOT NULL," \
			"  `mail_link` varchar(1024) NOT NULL," \
			"  `follow_num` varchar(32) NOT NULL," \
			"  `follower_num` varchar(32) NOT NULL," \
			"  `page_num` varchar(32) NOT NULL," \
			"  `words_num` varchar(32) NOT NULL," \
			"  `favored_num` varchar(32) NOT NULL," \
			"  PRIMARY KEY (`user_name`)" \
			") ENGINE=InnoDB"


	def getInsertSql(self):
		return "INSERT INTO author " \
              "(user_name, user_link, head_url, mail_link, follow_num, follower_num, page_num, words_num, favored_num) " \
              "VALUES (%(user_name)s, %(user_link)s, %(head_url)s, %(mail_link)s, %(follow_num)s, %(follower_num)s, %(page_num)s, %(words_num)s, %(favored_num)s)"






