# -*- coding:utf-8 -*-
import scrapy
from mySpider.items import ItcastItem


# 创建爬虫类
class ItcastSpider(scrapy.Spider):
    #爬虫名称
    name = "itcast"
    # 允许爬虫作用的范围
    allowed_domain = [
        "http://www.itcast.cn/"
    ]
    # 起始url
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#apm",
        "http://www.itcast.cn/channel/teacher.shtml#auids",
        "http://www.itcast.cn/channel/teacher.shtml#aLinux",
        "http://www.itcast.cn/channel/teacher.shtml#amovies",
        "http://www.itcast.cn/channel/teacher.shtml#atest",
        "http://www.itcast.cn/channel/teacher.shtml#apython",
        "http://www.itcast.cn/channel/teacher.shtml#arobot",
        "http://www.itcast.cn/channel/teacher.shtml#acloud",
        "http://www.itcast.cn/channel/teacher.shtml#anetmarket",
        "http://www.itcast.cn/channel/teacher.shtml#ac",
        "http://www.itcast.cn/channel/teacher.shtml#aweb",
        "http://www.itcast.cn/channel/teacher.shtml#aui",
        "http://www.itcast.cn/channel/teacher.shtml#ajavaee",
    ]

    def parse(self, response):
        # with open('teacher.html','w') as f :
        #     f.write(response.body)
        teacher_list = response.xpath('//div[@class="li_txt"]')
        items = []
        # 遍历根节点集合
        for each in teacher_list:
            item = ItcastItem()
            # 实例 item对象保存数据
            # 将匹配的内容(匹配对象)转为Unicode字符串
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()

            # print name[0]
            # print title[0]
            # print info[0]
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)

            # 将获得的值交给pipeline
            # yield item

        # 返回数据,不经过pipeline
        return items






