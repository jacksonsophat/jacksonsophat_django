# from django.shortcuts import get_object_or_404, render
# # from django.http import Http404
# from django.http import HttpResponse,HttpResponseRedirect
# # from django.template import loader
# from django.urls import reverse
# import feedparser
# from datetime import datetime
# import calendar
# import json
# from dateutil import tz
# import pytz

# def local_news():
#     data = [];
#     time_zone = pytz.timezone('America/Chicago')
#     # ABC Feed
#     KTRK = feedparser.parse("https://abc13.com/feed/")
#     KTRK_Entries = KTRK.entries
#     for item in KTRK_Entries:
#         date_string = item['published']
#         date_format = '%a, %d %b %Y %H:%M:%S %z'
#         time = datetime.strptime(date_string, date_format);
#         time = calendar.timegm(time.timetuple())
#         # change order of the time display
#         # time = time.astimezone(to_zone)
#         # time = time.strftime('%H:%M:%S %b/%d/%y')
#         # print(calendar.timegm(time.timetuple()))
#         try:
#             image = item['media_thumbnail'][0]['url']
#         except:
#             image = False
#             # image = 'images/no_img.jpg'
#         news = {
#         'station':'ABC13',
#         'title': item['title'],
#         'summary': item['summary'],
#         'link': item['link'],
#         'published': time,
#         'image': image
#         }
#         data.append(news)

#     # KHOU
#     KHOU = feedparser.parse("https://www.khou.com/feeds/syndication/rss/news/local")
#     KHOU_Entries = KHOU.entries  
#     # KHOU_logo = '/images/projects/local-news/khou.png'

#     for item in KHOU_Entries:
#         date_string = item['published']
#         # print(date_string)
#         date_format = '%a, %d %b %Y %H:%M:%S %Z'
#         time = datetime.strptime(date_string, date_format);
#         time = calendar.timegm(time.timetuple())

#         link = item['links'][0]['href']
#         try:
#             image = item['links'][1]['href']
#         except:
#             image = False
        
#         news = {
#             'station':'KHOU',
#             'title': item['title'],
#             'summary': item['summary'],
#             'link': link,
#             'published': time,
#             'image': image
#             }
#         data.append(news)

#     # NBC
#     KPRC = feedparser.parse("https://www.click2houston.com/arc/outboundfeeds/rss/category/news/local/?outputType=xml&size=10")
#     KPRC_Entries = KPRC.entries 
#     # KPRC_logo ='/images/projects/local-news/kprc.png'
#     for item in KPRC_Entries:
#         # image = item['media_content'][0]['url']
#         date_string = item['published']
#         date_format = '%a, %d %b %Y %H:%M:%S %z'
#         time = datetime.strptime(date_string, date_format);
#         time = calendar.timegm(time.timetuple())
        
#         # time = time.strftime('%H:%M:%S %b/%d/%y')
#         try:
#             image = item['media_content'][0]['url']
#         except:
#             image = False
#         news = {
#             'station':'KPRC',
#             'title': item['title'],
#             'summary': item['summary'],
#             'link': item['link'],
#             'published': time,
#             'image': image
#             }
#         data.append(news)   

#     # data.sort(key= lambda x: datetime.strftime(x['published'],'%H:%M:%S %b/%d/%y'))
#     data.sort(key= lambda x: x['published'], reverse=True)
#     for i in data:
#         # dt = datetime.fromtimestamp(i['published'], tz)
#         # print(dt.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
#         i['published'] = datetime.fromtimestamp(i['published'])
#         # print(datetime_object)
#         # i['published'] = datetime
#     return data;

# def my_test():
#     return 'Testing'