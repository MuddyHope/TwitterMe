from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponsePermanentRedirect


from .models import Tweets

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={} , status=200)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id" : tweet_id,
    }
    #status = 200
    try:
        obj = Tweets.objects.get(id = tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
    #status = 404
    
    return JsonResponse(data)