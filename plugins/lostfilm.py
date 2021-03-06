from core import downloader
from re import search

class lostfilm(downloader):
	def __init__(self):
		super().__init__()
		self.cookies = {'uid':'', 'pass':'', 'usess':''}
	def start(self):
		rss = self.parse('http://lostfilm.tv/rssdd.xml').rss('cp1251')
		if not rss:
			return 
		data = []
		for title, link in rss:
			try:
				s, e, sn, en = search('([^(]*) \([^)]*\)\. ([^(]*) \([^(]*\(S(\d+)E?(\d+)?', title).groups(1)
			except AttributeError:
				continue
			data.append({'quality':title, 'series':s, 'episode':e, 'episode_number':en, 'series_number':sn, 'link':link, 'extension':'torrent'})
		self.download(data, cookies=self.cookies)