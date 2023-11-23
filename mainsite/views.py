from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, AmazonPriceTracking
from django.urls import reverse
import feedparser
from datetime import datetime, timedelta
import calendar
import json
from dateutil import tz
import pytz
import requests
from bs4 import BeautifulSoup
import re
from django.shortcuts import redirect
from django.contrib import messages
import html
from .forms import AmazonForm, ContactUsForm
from datetime import date
import os
from .utils.zen_list import zen_items
# import lxml
# from .utils.utils import local_news, my_test


def homepage(request):
    meta_tags = {
        "page_title": 'Welcome',
        'meta_title': '',
        'meta_desc': ''
    }
    # pageTitle = 'Jackson Sophat | Welcome'
    # form = ContactUsForm()
    # if request.method == 'POST':
    #     form = ContactUsForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('form-submitted')
    # print(request.POST)
    context = {
        'page_title': meta_tags['page_title'],
        'meta_title': meta_tags['meta_title'],
        'meta_desc': meta_tags['meta_desc']
    }
    # context = {}
    return render(request, 'mainsite/homepage.html', context)


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def projects(request):
    return render(request, 'mainsite/projects/index.html')


def local_news(request):
    meta_tags = {
        "page_title": 'Local News',
        'meta_title': 'Keep yourself informed with your local news | Houston',
        'meta_desc': 'Stay Informed with the Latest News Headlines | Your one-stop destination for breaking news, trending stories, and updates from around the world. Get a comprehensive overview of current events, politics, entertainment, technology, and more, all in one place. Don\'t miss out on what\'s happening - browse our curated news headlines today.'
    }
    data = []
    time_zone = pytz.timezone('America/Chicago')
    # ABC Feed
    KTRK = feedparser.parse("https://abc13.com/feed/")
    KTRK_Entries = KTRK.entries
    for item in KTRK_Entries:
        date_string = item['published']
        date_format = '%a, %d %b %Y %H:%M:%S %z'
        time = datetime.strptime(date_string, date_format)
        time = calendar.timegm(time.timetuple())
        # change order of the time display
        # time = time.astimezone(to_zone)
        # time = time.strftime('%H:%M:%S %b/%d/%y')
        # print(calendar.timegm(time.timetuple()))
        try:
            image = item['media_thumbnail'][0]['url']
        except:
            image = False
            # image = 'images/no_img.jpg'
        news = {
            'station': 'ABC13',
            'title': item['title'],
            'summary': item['summary'],
            'link': item['link'],
            'published': time,
            'image': image
        }
        data.append(news)

    # KHOU
    KHOU = feedparser.parse(
        "https://www.khou.com/feeds/syndication/rss/news/local")
    KHOU_Entries = KHOU.entries
    # KHOU_logo = '/images/projects/local-news/khou.png'

    for item in KHOU_Entries:
        date_string = item['published']
        # print(date_string)
        date_format = '%a, %d %b %Y %H:%M:%S %Z'
        time = datetime.strptime(date_string, date_format)
        time = calendar.timegm(time.timetuple())

        link = item['links'][0]['href']
        try:
            image = item['links'][1]['href']
        except:
            image = False

        news = {
            'station': 'KHOU',
            'title': item['title'],
            'summary': item['summary'],
            'link': link,
            'published': time,
            'image': image
        }
        data.append(news)

    # NBC
    KPRC = feedparser.parse(
        "https://www.click2houston.com/arc/outboundfeeds/rss/category/news/local/?outputType=xml&size=10")
    KPRC_Entries = KPRC.entries
    # KPRC_logo ='/images/projects/local-news/kprc.png'
    for item in KPRC_Entries:
        # image = item['media_content'][0]['url']
        date_string = item['published']
        date_format = '%a, %d %b %Y %H:%M:%S %z'
        time = datetime.strptime(date_string, date_format)
        time = calendar.timegm(time.timetuple())

        # time = time.strftime('%H:%M:%S %b/%d/%y')
        try:
            image = item['media_content'][0]['url']
        except:
            image = False
        news = {
            'station': 'KPRC',
            'title': item['title'],
            'summary': item['summary'],
            'link': item['link'],
            'published': time,
            'image': image
        }
        data.append(news)

    # data.sort(key= lambda x: datetime.strftime(x['published'],'%H:%M:%S %b/%d/%y'))
    data.sort(key=lambda x: x['published'], reverse=True)
    for i in data:
        # dt = datetime.fromtimestamp(i['published'], tz)
        # print(dt.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
        i['published'] = datetime.fromtimestamp(i['published'])
        # print(datetime_object)
        # i['published'] = datetime
        print(i['published'])

    context = {
        'data': data,
        'page_title': meta_tags['page_title'],
        'meta_title': meta_tags['meta_title'],
        'meta_desc': meta_tags['meta_desc']
    }
    return render(request, 'mainsite/projects/local_news.html', context)


def amazon_price_tracking(request):
    output = {}
    if request.method == 'GET' and 'url' in request.GET:
        URL = request.GET["url"]
        # HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        #             'Accept-Language': 'en-US, en;q=0.5'})
        HEADERS={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        webpage = requests.get(URL, headers=HEADERS)
        if (webpage.status_code != 200):
            print('Webpage')
            print(webpage)
            # throw error here
        print(webpage.status_code)
        soup = BeautifulSoup(webpage.content, "html.parser")
        print(soup)
        # print(0)
        output['url'] = URL
        try:
            output["title"] = soup.find(
                'h1', {'id': 'title'}).text.strip()
            print('here')
            # output["title"] = soup.find(
            #     'span', {'id': 'productTitle'}).text.strip()
            print(1)
        except:
            print("No Title")
            # output["title"] = None

        images = re.findall('"hiRes":"(.+?)"', webpage.text)
        if (len(images) > 0):
            output["images"] = images
            print(2)

        try:
            output["price"] = soup.find(
                "span", {"class": "a-price"}).find("span").text
            print(3)

        except:
            print("No price")
    else:
        url = ""

    if request.method == 'POST':
        form_name = html.escape(request.POST['name']) 
        # print(form_name)
        # if form_name == '':
        #     messages.error(request, 'Name cannot be empty!')
        #     return redirect('amazon')
        form_url = html.escape(request.POST['url'])
        form_current_price = html.escape(request.POST['current_price'])
        form_tracking_price = html.escape(request.POST['tracking_price'])
        form_expired_date = int(html.escape(request.POST['expired_date'])) * 7
        # return
        if(form_expired_date):
            form_expired_date = datetime.date(datetime.now()) + timedelta(days=form_expired_date)
            # print(form_expired_date)
            # messages.success(request, 'Return')
            # return redirect('amazon')
        form_contact_method = html.escape(request.POST['contact_method'])
        form_phone = html.escape(request.POST['phone'])
        form_email = html.escape(request.POST['email'])
        data = AmazonPriceTracking.objects.create(
            url=form_url,
            name=form_name,
            current_price=form_current_price, 
            tracking_price=form_tracking_price,
            contact_method=form_contact_method,
            email=form_email,
            phone=form_phone,
            expired_date = form_expired_date)
        # print(form)
        # print(form['phone'])
        # if form.is_valid():
        #     print('Valid')
        # else :
        #     print(form.errors)

        messages.success(request, 'Saved!')
        return redirect('amazon')
        # validate all those info make sure they exist
        # redirect to a thank you page
    # form = AmazonForm()
    context = {
        'output': output
    }
    # print(context)

    return render(request, 'mainsite/projects/amazon/amazon.html', context)


def zen(request):
    items = zen_items
    print(items)
    context = {
        'page_title': 'Zen - Guided Meditations, Nature Sounds, and Breathing Exercises for Relaxation',
        'meta_title': 'Experience Tranquility with Zen: Guided Meditations, Nature Sounds, and Breathing Exercises',
        'meta_desc': 'Discover tranquility with Zen - your personalized oasis for guided meditations, soothing nature sounds, and mindful breathing exercises. Immerse yourself in a world of relaxation, track your progress, and share the journey with a supportive community. Cultivate mindfulness effortlessly with our diverse library of calming audio experiences. Elevate your well-being – one breath at a time.',
        'items':items
    }
    return render(request, 'mainsite/projects/zen.html', context)


def contact(request):
    form = ContactUsForm
    if request.method == 'POST':                   
        form = ContactUsForm(request.POST)
        if form.is_valid():                          
            form.save()                              
        return redirect('thank_you') 
    context = {
        'page_title': 'Thank You for Your Support - Jackson Sophat ',
        'form':form
    }
    return render(request, 'mainsite/contact/contact_us.html', context)


def thank_you(request):
    context = {
        # 'data': data,
        # 'page_title': meta_tags['page_title'],
        # 'meta_title': meta_tags['meta_title'],
        # 'meta_desc': meta_tags['meta_desc'],
    }
    return render(request, 'mainsite/contact/thank_you.html', context)


# Testing Page
def testing_page(request):
    # my_list = [
    #     {'pub':'22:30:14 Oct/18/23'},
    #     {'pub':'17:01:17 Oct/18/23'},
    #     {'pub':'21:59:38 Oct/18/23'}
    # ]
    # my_data = my_list.sort(key= lambda x: x['pub'])
    # data = my_data
    data = local_news()
    print(data)
    context = {'data': data
               }
    return render(request, 'mainsite/testing_page.html', context)
