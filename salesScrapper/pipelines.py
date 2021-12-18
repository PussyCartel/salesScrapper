# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2


class PostgreSQKPIPELINE(object):

    def open_spider(self, spider):
        hostname = '178.216.96.119'
        username = 'postgres'
        password = 'q4X3YaTh4XeVk5Z'
        database = 'postgres'
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password,
            dbname=database)
        self.cur = self.connection.cursor()  # Define function to disconnect from database

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()  # Define function to process each scraped item and insert it into    PostgreSQL table

    def process_item(self, item, spider):
        try:
            # Execute SQL command on database to insert data in table
            self.cur.execute(
                "insert into DeliveryPayAttentionBlock (product_name, product_company) values(%s,%s)",
                (item['product_name'], item['product_company']))
            self.connection.commit()
        except:
            self.connection.rollback()
            raise
            return item
