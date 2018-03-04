# -- coding: utf-8 --

import scrapy

class BaseItem(scrapy.Item):

	def insertToDb(self, mysqldb):
		table_sql = self.getTableSql()
		insert_sql = self.getInsertSql()
		if table_sql and insert_sql:
			# print 'createTable: ', table_sql
			# print 'insert: ', insert_sql
			# print dict(self)
			mysqldb.createTable(table_sql)
			mysqldb.insert(insert_sql, dict(self))
		else:
			print 'Empty!!!!!!!!!!!!!!!!!!!!!!!'
		pass

	def getTableSql(self):
		return None

	def getInsertSql(self):
		return None