# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import pymysql
from scrapy_deomo1.settings import MYSQL
class ScrapyDeomo1Pipeline:
    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        sql = "insert into novel (title, image_path_local, introduce,image_path_network) values (%s, %s, %s,%s)"
        cursor.execute(sql, (item['title'], item['image_path'], item['introduction'], item['image_src']))
        self.conn.commit()
        return item
    def open_spider(self, spider):
        print('here')
        self.conn = pymysql.connect(host=MYSQL['host'],
                port=MYSQL['port'],
                user=MYSQL['username'],
                password=MYSQL['password'],
                database=MYSQL['database']
                )
    def close_spider(self, spider):
        if self.conn:
            self.conn.close()

class MYImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 负责下载
        return scrapy.Request(item['image_src'])
    def file_path(self, request, response=None, info=None, *, item=None):
        # 准备文件名
        file_name = request.url.split('/')[-1].split('-')[0]
        return f'./img/{file_name}'
    def item_completed(self, results, item, info):
        # 返回文件下载的详细信息
        print(results)
        ok, finfo = results[0]
        item['image_path'] = finfo["path"]
        return item