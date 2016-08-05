# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeatherPipeline(object):
	def __init__(self):
		pass
	def process_item(self, item, spider):
		with open('wea.txt','w+') as file:
			city=item['city'][0]
			date=item['date']
			desc=item['dayDesc']
			dayTemp=item['dayTemp']

			flag=True # True stands for day, False means Night
			flag=not len(desc)%2
			if flag:
				dayDesc=desc[0::2]
				nightDesc=desc[1::2]
			else:
				dayDesc=[' ']+desc[1::2]
				nightDesc=desc[0::2]

			weaitem=zip(date,dayDesc,nightDesc,dayTemp)
			if not flag:
				item=weaitem[0]
				txt='date:{0}\t\tnight:{1}({2})\n\n'.format\
				(item[0].encode('utf-8'),item[2].encode('utf-8'),item[3].encode('utf-8'))
				file.write(txt)
				weaitem=weaitem[1:]
			for i in range(len(weaitem)):
				item=weaitem[i]
				ta=item[3].split('/')
				dt=ta[0]
				nt=ta[1]
				txt='date:{0}\t\tday:{1}({2})\t\tnight:{3}({4})\n\n'.format\
				(item[0].encode('utf-8'),item[1].encode('utf-8'),dt.encode('utf-8'),\
				item[2].encode('utf-8'),nt.encode('utf-8'))
				file.write(txt)

			return item


