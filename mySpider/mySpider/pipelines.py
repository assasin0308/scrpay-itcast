# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json
class ItcastPipeline(object):
    # 可选择 初始化类
    def __init__(self):
        self.filename = open('itcast-teahcer.json','w')

    # 必须 处理item数据的方法
    def process_item(self,item,spider):

        json_txt = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.filename.write(json_txt.encode('utf-8'))
        return item

    # 可选择 最后执行 关闭spider
    def close_spider(self,spider):
        self.filename.close()

