from django.shortcuts import render
import requests, json

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
            'maxResults' : 10,
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
            videos.append(video_data)
        

    context = {
        'videos' : videos
    }
    
    return render(request, 'ytsearch/index.html', context)
