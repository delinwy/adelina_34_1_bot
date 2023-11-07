# import httpx
# from parsel import Selector
# import asyncio
#
#
# class AsyncNewsScraper:
#     HEADERS = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#         'Accept-Language': 'en-GB,en;q=0.5',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Connection': 'keep-alive'
#     }
#     URL = 'https://rezka.ag/animation/page/{page}/'
#     LINK_XPATH = '//div[@class="b-content__inline_item-link"]/a/@href'
#     PLUS_URL = 'https://rezka.ag'
#
#     async def async_generator(self, limit):
#         for page in range(1, limit + 1):
#             yield page
#
#     async def parse_pages(self):
#         async with httpx.AsyncClient(headers=self.HEADERS) as client:
#             async for page in self.async_generator(limit=3):
#                 await self.get_url(
#                     client=client,
#                     url=self.URL.format(
#                         page=page
#                     )
#                 )
#
#     async def get_url(self, client, url):
#         response = await client.get(url)
#         print(response.url)
#         await self.scrape_links(html=response.text, client=client)
#
#     async def scrape_links(self, html, client):
#         tree = Selector(text=html)
#         links = tree.xpath(self.LINK_XPATH).extract()[:5]
#         for link in links:
#             print(link)
#
#
# if __name__ == '__main__':
#     scraper = AsyncNewsScraper()
#     asyncio.run(scraper.parse_pages())
