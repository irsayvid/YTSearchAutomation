from django.shortcuts import render
import requests, json
from .models import SearchResults
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    videos = []
    keys_file = open('./ytsearch/apikeys.json')
    keys = json.load(keys_file)["keys"]
    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        search_query = request.POST['search']
        if search_query == '' or search_query is None:
            search_query = "chess"

        search_params = {
            'publishedAfter': '2002-01-01T00:00:00Z',
            'order':'date', # sorted in reverse chronological order
            'part' : 'snippet',
            'q' : search_query,
            'key' : keys[0],
            'maxResults' : 15,
            'type' : 'video',
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()["items"]
        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'description' : result['snippet']['description'],
                'video_id' : result['id']['videoId'],
                'publish_datetime' : result['snippet']['publishedAt'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"]["videoId"] }',
                'thumbnail' : result['snippet']['thumbnails']['high']['url'],
            }
            store = SearchResults(video_id = video_data['video_id'], title = video_data['title'], description = video_data['description'], search_query = search_query, publish_datetime = video_data['publish_datetime'], thumbnail_url = video_data['thumbnail'])
            store.save()
            videos.append(video_data)
        

    context = {
        'videos' : videos
    }
    
    return render(request, 'ytsearch/index.html', context)

def fetchstored(request, page=1):
    response = list(SearchResults.objects.order_by("-publish_datetime"))
    paginator = Paginator(response, 8)
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        # if we exceed the page limit we return the last page 
        response = paginator.page(paginator.num_pages)
    context = {"response":response}
    return render(request, 'ytsearch/fetchresults.html', context)

def fetchstored(request, query="", page=1):
    response = SearchResults.objects.order_by("-publish_datetime")
    if query is None or query != "":
        response = response.filter(search_query=query)
    paginator = Paginator(response, 8)
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        # if we exceed the page limit we return the last page 
        response = paginator.page(paginator.num_pages)
    context = {"response":response}
    return render(request, 'ytsearch/fetchresults.html', context)
