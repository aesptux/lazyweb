from lazyweb.apps.lazytweets.models import Tweet
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def show_lazy_people(request):  # with love :)
    lazy_tweets = Tweet.objects.all().order_by('-id')
    paginator = Paginator(lazy_tweets, 15)
    page = request.GET.get('page')
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tweets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tweets = paginator.page(paginator.num_pages)

    return render_to_response("index.html", {'tweets': tweets})
