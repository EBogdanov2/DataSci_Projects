# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo 
import logging

from scrapy.utils.project import get_project_settings 
from scrapy.exceptions import DropItem

from itemadapter import ItemAdapter

settings = get_project_settings() 

# Create the pipeline class for the database
class PgaEtlPipeline: 
    def __init__(self):
        # Connect to the database outlined in settings.py
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    # Add the scraped items from the Spider class into the database
    def process_item(self, item, spider): 
        valid = True
        for data in item: 
            if not data: 
                valid = False 
                raise DropItem("Missing {0}!".format(data))
            if valid: 
                self.collection.insert(dict(item))
                logging.log(msg="Stat added to the database",level = logging.DEBUG, spider = spider)
        return item