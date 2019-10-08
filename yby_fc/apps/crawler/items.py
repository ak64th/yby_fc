import scrapy


class BilibiliVideoItem(scrapy.Item):
    video_id = scrapy.Field()
    title = scrapy.Field()
    up_name = scrapy.Field()
    member_id = scrapy.Field()
    watch_num = scrapy.Field()
    pub_date = scrapy.Field()
