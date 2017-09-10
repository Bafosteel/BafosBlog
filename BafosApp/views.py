from django.shortcuts import render
from .models import BlogPost,Category
from django.shortcuts import get_object_or_404, render_to_response
# Create your views here.

def index(request):
    entries = BlogPost.objects.published()
    return render_to_response('BafosApp/index.html', {'entries': entries})

def category(request, id, slug):
    category = get_object_or_404(Category, id=id, slug=slug)
    entries = category.entries.published()
    return render_to_response('BafosApp/index.html', {'entries': entries})


def archive_year(request, year):
    entries = BlogPost.objects.filter(draft=False,
                                      published_date__year=year)
    return render_to_response('BafosApp/index.html', {'entries': entries})


def archive_month(request, year, month):
    entries = BlogPost.objects.filter(draft=False,
                                      published_date__year=year,
                                      published_date__month=month)
    return render_to_response('BafosApp/index.html', {'entries': entries})


def archive_day(request, year, month, day):
    entries = BlogPost.objects.filter(draft=False,
                                      published_date__year=year,
                                      published_date__month=month,
                                      published_date__day=day)
    return render_to_response('BafosApp/index.html', {'entries': entries})


def details(request, year, month, day, slug):
    entry = get_object_or_404(BlogPost, draft=False,
                              published_date__year=year,
                              published_date__month=month,
                              published_date__day=day,
                              slug=slug)
    return render_to_response('BafosApp/details.html', {'entry': entry})