class BilibiliPipeline(object):
    def process_item(self, item, spider):
        print(item['video_id'], item['title'], item['pub_date'])
        return item
