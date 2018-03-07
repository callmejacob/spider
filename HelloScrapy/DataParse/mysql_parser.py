# -- coding: utf-8 --

import mysql.connector
import jieba
import jieba.posseg as pseg
import json
import operator

# 解决UnicodeWarning问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 初始化中文分词器
jieba.initialize()

HP_DESC = {
	u'Ag' : '形语素',
	u'n'  : '名词',
	u'v'  : '动词',
	u'x'  : '非语素字',
	u'r'  : '代词',
	u'm'  : '数词',
	u'd'  : '副词',
	u'a'  : '形容词',
	u'nr' : '人名',
	u'p'  : '介词',
	u'c'  : '连词',
	u't'  : '时间词',
	u'ns' : '地名',
	u'f'  : '方位词',
	u'i'  : '成语',
	u'l'  : '习用语',
	u'vn' : '名动词',
	u'y'  : '语气词',
	u'u'  : '助词',
	u'nz' : '其他专名',
	u's'  : '处所词',
	u'q'  : '量词',
}

def getHpDesc(hp):
	if hp in HP_DESC:
		return HP_DESC[hp]
	else:
		return hp

def printHpItems(sorted_items, result_hp, hp_desc, size=-1):
	print hp_desc
	print '---' * 20
	count = 0;
	for item in sorted_items:
		word = item[0]
		val = item[1]
		hp = ''
		if word in result_hp:
			hp = result_hp[word]
		if getHpDesc(hp) == hp_desc:
			print '{:<10s}{:d}'.format(word, val)
			if size > 0:
				count += 1
				if (count > size):
					break
	print '---' * 20
	print '\n\n'

def stat_topic(topic):

	# 打开数据库
	cnx = mysql.connector.connect(user='xxx', password='xxx', database='jianshu')
	cursor = cnx.cursor()

	# 分条拉取
	result = {}
	result_hp = {}
	hp_stat = {}

	cursor.execute("SELECT title,read_num,reply_num,favor_num FROM article_desc WHERE topic='{}' ORDER BY title ASC".format(topic))
	for title, read_num, reply_num, favor_num in cursor:
		words = jieba.cut(title, cut_all = False)
		for word in words:
			if word in result:
				result[word] += int(read_num)
			else:
				result[word] = int(read_num)

		# 词性分析
		words = pseg.cut(title)
		for word, flag in words:
			result_hp[word] = flag
			if flag in hp_stat:
				hp_stat[flag] += 1
			else:
				hp_stat[flag] = 1

	# 排序
	# sorted(result.items(),key = lambda x:x[1],reverse = True)
	sorted_items = sorted(result.items(),key = operator.itemgetter(1), reverse = True)
	sorted_hp = sorted(hp_stat.items(),key = operator.itemgetter(1), reverse = False)

	# 打印
	printHpItems(sorted_items, result_hp, '名词', 30)
	printHpItems(sorted_items, result_hp, '动词', 30)

	# for item in sorted_hp:
	# 	hp = item[0]
	# 	val = item[1]
	# 	print getHpDesc(hp), val

	# 记录result
	file = open('result.txt', 'w')
	line = json.dumps(result)
	file.write(line)
	file.close()

	# 关闭数据库
	cursor.close()
	cnx.close()

# 测试程序
stat_topic('故事')