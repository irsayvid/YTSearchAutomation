from django.shortcuts import render
from django.db.models import Q
import requests, json
from .models import SearchResults
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def ytsearch(key, query="chess"):
#     search_url = 'https://www.googleapis.com/youtube/v3/search'
#     search_params = {
#             'publishedAfter': '2002-01-01T00:00:00Z',
#             'order':'date', # sorted in reverse chronological order
#             'part' : 'snippet',
#             'q' : query,
#             'key' : key,
#             'maxResults' : 15,
#             'type' : 'video',
#         }
#     r = requests.get(search_url, params=search_params)
#     return r.json()


def index(request):
    videos = []
    keys_file = open('./ytsearch/apikeys.json')
    keys = json.load(keys_file)["keys"]
    if request.method == 'POST':
        search_query = request.POST['search']
        i = 0
        while (i < len(keys)):
            if search_query == "" or search_query is None:
                search_query = "chess"
                # results = ytsearch( keys[i])
            # else:
                # results = ytsearch( keys[i], search_query)
            try: 
                search_url = 'https://www.googleapis.com/youtube/v3/search'
                search_params = {
                        'publishedAfter': '2002-01-01T00:00:00Z',
                        'order':'date', # sorted in reverse chronological order
                        'part' : 'snippet',
                        'q' : search_query,
                        'key' : keys[i],
                        'maxResults' : 15,
                        'type' : 'video',
                    }
                r = requests.get(search_url, params=search_params)
                results = r.json()
                for result in results["items"]:
                    video_data = {
                        'title' : result['snippet']['title'],
                        'description' : result['snippet']['description'],
                        'video_id' : result['id']['videoId'],
                        'publish_datetime' : result['snippet']['publishedAt'],
                        'url' : f'https://www.youtube.com/watch?v={ result["id"]["videoId"] }',
                        'thumbnail' : result['snippet']['thumbnails'],
                    }
                    store = SearchResults(video_id = video_data['video_id'], title = video_data['title'], description = video_data['description'], search_query = search_query, publish_datetime = video_data['publish_datetime'], thumbnail_url = video_data['thumbnail'])
                    store.save()
                    videos.append(video_data)
                break # can return result here to stop continuous requests
            except:
                print("status code: {} \nmessage: {}".format(results["error"]["code"],results["error"]["message"]))
                i += 1

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
    print(query,page)
    if (query is None) or (query != "" and query!="_all"):
        response = response.filter(Q(title__icontains=query)|Q(search_query__icontains=query))
    else:
        query="_all"
    paginator = Paginator(response, 8)
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        # if we exceed the page limit we return the last page 
        response = paginator.page(paginator.num_pages)
    context = {"response":response, "query":query}
    return render(request, 'ytsearch/fetchresults.html', context)
