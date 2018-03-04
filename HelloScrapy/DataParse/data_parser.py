# -- coding: utf-8 --

import json

def printAuthor(item):
	print '\n'
	print item['name']
	print item['text_num']
	print item['favor_num']
	pass

def printArticle(item):
	print '\n'
	print item['title']
	print item['author']
	print item['author_link']
	print item['content']
	pass

def printArticleDesc(item):
	print '\n'
	print item['author']
	print item['time']
	print item['title']
	print item['link']
	print item['abstract']
	print item['read_num']
	print item['reply_num']
	item['favor_num']
	pass

'''
主程序
'''
items_file = open('items.txt')
items_content = items_file.read()

# 解析字符串数组
items = items_content.split('}')
for i in range(len(items)):
	if len(items[i]) > 0:
		if not items[i].endswith('"'):
			items[i] += '"'
		items[i] += '}'

# json化
objs = []
for item in items:
	if len(item) > 0:
		try:
			objs.append(json.loads(item))
		except ValueError:
			continue

# 解析json
article_list = []
article_desc_list = []
author_list = []
for obj in objs:
	if not 'item_type' in obj:
		continue
	
	item_type = obj['item_type']
	if item_type == 'article':
		article_list.append(obj)
	elif item_type == 'article_desc':
		article_desc_list.append(obj)
	elif item_type == 'author':
		author_list.append(obj)


# 打印
for item in article_list:
	printArticle(item)

for item in article_desc_list:
	printArticleDesc(item)

for item in author_list:
	printAuthor(item)