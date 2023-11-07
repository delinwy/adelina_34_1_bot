# from parsel import Selector
# import requests
#
#
# class NewsScraper:
#     URL = 'https://www.riotgames.com/en/news'
#     LINK_XPATH = '//div[@class="summary"]/a/@href'
#     PLUS_URL = 'https://www.riotgames.com'
#
#     def parse_data(self):
#         html = requests.get(url=self.URL).text
#         tree = Selector(text=html)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         for link in links:
#             print(self.PLUS_URL + link)
#
#         return links[:5]
#
#
# if __name__ == '__main__':
#     scraper = NewsScraper()
#     scraper.parse_data()
