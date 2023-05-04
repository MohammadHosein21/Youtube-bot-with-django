from googleapiclient.discovery import build
import urllib.parse
from .models import Channel


# دریافت کلمه از کاربر
# search_term = input("Enter the search term: ")

# ایجاد ارتباط با API یوتیوب
# api_key = "AIzaSyDeAmMZ6raZiZkWi_AgLVIIq1kg9Pb7rP8"
# youtube = build('youtube', 'v3', developerKey=api_key)

# جستجوی کانال‌های مرتبط با کلمه

# query = urllib.parse.quote(search_term)
# request = youtube.search().list(
#     part="id,snippet",
#     maxResults=50,
#     type='channel',
#     q=query,
#     order='relevance'
# )
# response = request.execute()
# nextPage = response['nextPageToken']
# print(response['nextPageToken']
# نمایش عنوان، تعداد فالورها و لینک اشتراک هر کانال
# count = 0
# for item in response['items']:
#     channelId = item['id']['channelId']
#     channelTitle = item['snippet']['title']
#
#     request = youtube.channels().list(
#         part="statistics",
#         id=channelId
#     )
#     response = request.execute()
#
#     subscriberCount = response['items'][0]['statistics']['subscriberCount']
#     channelUrl = f"https://www.youtube.com/channel/{channelId}"
#
#     print(f"Channel Title: {channelTitle}\nSubscriber Count: {subscriberCount}\nChannel URL: {channelUrl}\n")
#     count += 1
# print(count)
# print("###########################################################")
# if nextPage == 'CDIQAA':
#     request = youtube.search().list(
#         part="id,snippet",
#         maxResults=50,
#         type='channel',
#         q=query,
#         pageToken='CDIQAA',
#         order='relevance'
#     )
#     response = request.execute()
# print(response['nextPageToken'])
# for item in response['items']:
#     channelId = item['id']['channelId']
#     channelTitle = item['snippet']['title']
#
#     request = youtube.channels().list(
#         part="statistics",
#         id=channelId
#     )
#     response = request.execute()
#
#     subscriberCount = response['items'][0]['statistics']['subscriberCount']
#     channelUrl = f"https://www.youtube.com/channel/{channelId}"
#
#     print(f"Channel Title: {channelTitle}\nSubscriber Count: {subscriberCount}\nChannel URL: {channelUrl}\n")
#     count += 1
#
# print(count)


def search(keyword):
    api_key = "AIzaSyDeAmMZ6raZiZkWi_AgLVIIq1kg9Pb7rP8"
    youtube = build('youtube', 'v3', developerKey=api_key)
    query = urllib.parse.quote(keyword)
    request = youtube.search().list(
        part="id,snippet",
        maxResults=50,
        type='channel',
        q=query,
        order='relevance'
    )
    response = request.execute()
    if 'nextPageToken' in response:
        nextPage = response['nextPageToken']
        for item in response['items']:
            channelId = item['id']['channelId']
            channelTitle = item['snippet']['title']

            request = youtube.channels().list(
                part="statistics",
                id=channelId
            )
            response = request.execute()

            subscriberCount = response['items'][0]['statistics']['subscriberCount']
            channelUrl = f"https://www.youtube.com/channel/{channelId}"

            Channel.objects.create(title=channelTitle, subscriber=subscriberCount, link=channelUrl, keyword=keyword)

        # if 'nextPageToken' in response:
        if nextPage == 'CDIQAA':
            request = youtube.search().list(
                part="id,snippet",
                maxResults=50,
                type='channel',
                q=query,
                pageToken='CDIQAA',
                order='relevance'
            )
            response = request.execute()
        for item in response['items']:
            channelId = item['id']['channelId']
            channelTitle = item['snippet']['title']

            request = youtube.channels().list(
                part="statistics",
                id=channelId
            )
            response = request.execute()

            subscriberCount = response['items'][0]['statistics']['subscriberCount']
            channelUrl = f"https://www.youtube.com/channel/{channelId}"

            Channel.objects.create(title=channelTitle, subscriber=subscriberCount, link=channelUrl, keyword=keyword)

        return Channel.objects.filter(keyword=keyword).order_by('-subscriber')

    else:
        for item in response['items']:
            channelId = item['id']['channelId']
            channelTitle = item['snippet']['title']

            request = youtube.channels().list(
                part="statistics",
                id=channelId
            )
            response = request.execute()

            subscriberCount = response['items'][0]['statistics']['subscriberCount']
            channelUrl = f"https://www.youtube.com/channel/{channelId}"

            Channel.objects.create(title=channelTitle, subscriber=subscriberCount, link=channelUrl, keyword=keyword)
        return Channel.objects.filter(keyword=keyword).order_by('-subscriber')
