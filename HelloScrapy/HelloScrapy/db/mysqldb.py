# -- coding: utf-8 --

import mysql.connector
from mysql.connector import errorcode

from settings import *

class MySqlDb(object):

	def __init__(self, db_name):
		self.db_name = db_name
		self.cnx = None
		self.cursor = None
		pass

	def open(self):
		self.cnx = mysql.connector.connect(user=MYSQL_USER_NAME, password=MYSQL_PASS_WORD)
		self.cursor = self.cnx.cursor()
		self.__ensureDb(self.cnx, self.cursor, self.db_name)
		pass

	def close(self):
		if self.cursor:
			self.cursor.close()
		if self.cnx:
			self.cnx.close()
		pass

	def createTable(self, tbl_ddl):
		if self.cnx and self.cursor:
			self.__ensureDb(self.cnx, self.cursor, self.db_name)
			self.__ensureTable(self.cursor, tbl_ddl)
		pass

	def insert(self, sql, values):
		if self.cnx and self.cursor:
			try:
				self.cursor.execute(sql, values)
				self.cnx.commit()
			except:
				pass
		pass

	def __ensureDb(self, cnx, cursor, db_name):
		try:
			cnx.database = db_name
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_BAD_DB_ERROR:
				try:
					cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
				except mysql.connector.Error as create_err:
					print("Failed creating database: {}".format(create_err))
					exit(1)
				cnx.database = db_name
			else:
				print err
				exit(1)

	def __ensureTable(self, cursor, tbl_ddl):
		try:
			cursor.execute(tbl_ddl)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
				pass
			else:
				print err.msg
		else:
			pass

