# -- coding: utf-8 --

import scrapy

from HelloScrapy.items import *

from urlparse import urljoin

root_url = 'http://www.jianshu.com'

class DemoScrapy(scrapy.Spider):
	name = 'demo'
	allowed_domains = ['jianshu.com']
	start_urls = [
		# 'https://www.jianshu.com/u/4a4eb4feee62',
		# 'https://www.jianshu.com/u/d2a08403ea7f',
		# 'https://www.jianshu.com/u/6a302f979011',
		# 'https://www.jianshu.com/c/dqfRwQ',
		'https://www.jianshu.com/c/fcd7a62be697',
	]

	def parse(self, response):
		cur_url = response.url
		print '###' * 10
		print cur_url
		print '###' * 10

		if cur_url.startswith('https://www.jianshu.com/u'):
			main_top_sel = response.xpath("//body/div/div/div/div[@class='main-top']")
			user_link = main_top_sel.xpath("a[@class='avatar']/@href").extract()[0]
			user_link = urljoin(root_url, user_link)
			head_url = main_top_sel.xpath("a[@class='avatar']/img/@src").extract()[0]
			head_url = head_url[2:]
			mail_link = main_top_sel.xpath("a/@href")[1].extract()
			mail_link = urljoin(root_url, mail_link)
			user_name = main_top_sel.xpath("div[@class='title']/a/text()").extract()[0]
			follow_num = main_top_sel.xpath("div[@class='info']/ul/li/div/a/p/text()").extract()[0]
			follower_num = main_top_sel.xpath("div[@class='info']/ul/li/div/a/p/text()").extract()[1]
			page_num = main_top_sel.xpath("div[@class='info']/ul/li/div/a/p/text()").extract()[2]
			words_num = main_top_sel.xpath("div[@class='info']/ul/li/div/p/text()").extract()[0]
			favored_num = main_top_sel.xpath("div[@class='info']/ul/li/div/p/text()").extract()[1]

			for page_sel in response.xpath('//body/div/div/div/div/ul/li'):
				name = page_sel.xpath('div/a/text()').extract()[0]
				link = page_sel.xpath('div/a/@href').extract()[0]
				read_num = page_sel.xpath('div/div/a/text()')[3].extract()
				favor_num = page_sel.xpath('div/div/a/text()')[5].extract()

				link = urljoin('http://www.jianshu.com', link)
				read_num = read_num[1:len(read_num)-1]
				favor_num = favor_num[1:len(favor_num)-1]

				# 继续抓取
				yield scrapy.Request(url=link, callback=self.parse)

				print '-*-' * 30
				print name
				print link
				print read_num
				print favor_num

			print '-*-' * 30


			item = AuthorItem()
			item['item_type']    = 'author'
			item['user_name']    = user_name
			item['user_link']    = user_link
			item['head_url']     = head_url
			item['mail_link']    = mail_link
			item['follow_num']   = int(follow_num)
			item['follower_num'] = int(follower_num)
			item['page_num']     = int(page_num)
			item['words_num']    = int(words_num)
			item['favored_num']  = int(favored_num)
			yield item
		elif cur_url.startswith('https://www.jianshu.com/p'):
			article_sel = response.xpath('//body/div[@class="note"]/div[@class="post"]/div[@class="article"]')

			title = article_sel.xpath("h1[@class='title']/text()")[0].extract()
			author = article_sel.xpath("div[@class='author']/div[@class='info']/span/a/text()")[0].extract()
			author_link = article_sel.xpath("div[@class='author']/div[@class='info']/span/a/@href")[0].extract()
			author_link = urljoin('http://www.jianshu.com', author_link)

			content = article_sel.xpath("div[@class='show-content']/div[@class='show-content-free']/*").extract()
			content = article_sel.xpath("div[@class='show-content']/div[@class='show-content-free']//text()").extract()
			content = ''.join(content)

			# print '-*-' * 30
			# print title
			# print author
			# print author_link
			# print content
			# print '-*-' * 30
			# print ''

			item = ArticleItem()
			item['item_type'] = 'article'
			item['title'] = title
			item['author'] = author
			item['author_link'] = author_link
			item['content'] = content
			yield item

			yield scrapy.Request(url=author_link, callback=self.parse)

		elif cur_url.startswith('https://www.jianshu.com/c'):
			if not '?' in cur_url:
				# 最新收录文章
				for i in range(2):
					page_url = '%s?order_by=added_at&page=%d' % (cur_url, i)
					yield scrapy.Request(url=page_url, callback=self.parse)
			else:
				main_sel = response.xpath('//body/div/div/div')[0]
				top_sel = main_sel.xpath('div')[0]
				list_sel = main_sel.xpath('div')[1]

				c_title = top_sel.xpath('div')[1].xpath('a/text()').extract()[0]
				c_info = top_sel.xpath('div/text()')[2].extract()
				c_info = c_info[11:len(c_info)-9]

				c_notelist = list_sel.xpath('ul/li/div')
				for note_sel in c_notelist:
					author = note_sel.xpath('div/div/a/text()')[0].extract()
					time = note_sel.xpath('div/div/span/@data-shared-at')[0].extract()
					title = note_sel.xpath('a/text()')[0].extract()
					link = note_sel.xpath('a/@href')[0].extract()
					link = urljoin('http://www.jianshu.com', link)
					abstract = note_sel.xpath('p/text()')[0].extract()
					abstract = abstract[7:len(abstract)-5]
					read_num = note_sel.xpath('div')[1].xpath('a')[0].xpath('text()')[1].extract()
					read_num = read_num[1:len(read_num)-1]
					reply_num = note_sel.xpath('div')[1].xpath('a')[1].xpath('text()')[1].extract()
					reply_num = reply_num[1:len(reply_num)-1]
					favor_num = note_sel.xpath('div')[1].xpath('span/text()')[0].extract()
					favor_num = favor_num[1:]

					# 继续抓取
					yield scrapy.Request(url=link, callback=self.parse)

					print '-*-' * 30
					print author
					print time
					print title
					print link
					print abstract
					print read_num
					print reply_num
					print favor_num

					item = ArticleDescItem()
					item['item_type'] = 'article_desc'
					item['topic'] = c_title
					item['author'] = author
					item['time'] = time
					item['title'] = title
					item['link'] = link
					item['abstract'] = abstract
					item['read_num'] = read_num
					item['reply_num'] = reply_num
					item['favor_num'] = favor_num
					yield item

				print '-*-' * 30



