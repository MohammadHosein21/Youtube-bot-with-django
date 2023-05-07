from googleapiclient.discovery import build
import urllib.parse
from .models import Channel


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
