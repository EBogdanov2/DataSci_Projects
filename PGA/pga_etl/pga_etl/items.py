import scrapy

from scrapy.item import Item, Field

# Define the stats that are to be extracted for the database
class PgaEtlItem(Item):
    name = Field() # player name
    rank = Field() # rank for specified stat
    distance = Field() # distance off the tee
    tournament = Field() # tournament statistic was recorded in
    pass