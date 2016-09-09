from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Blog, Link
from rest_framework import viewsets
from .serializers import BlogSerializer, LinkSerializer
import json

class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer

class LinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Link.objects.all().order_by('id')
    serializer_class = LinkSerializer

def index(request):
    context = {
        'blogs_length': len(Blog.objects.all()),
        'links_length': len(Link.objects.all()),
        'blog_page_count': (len(Blog.objects.all()) - 1) // 20 + 1,
    }
    return render(request, 'crawl/index.html', context)

def in_degrees(request, page):
    sorted_in_degrees = Paginator(Blog.objects.order_by('-in_degree'), 20)
    p = sorted_in_degrees.page(page).object_list
    p = list(map(lambda a: a.id, p))
    return HttpResponse(json.dumps(p))

def out_degrees(request, page):
    sorted_out_degrees = Paginator(Blog.objects.order_by('-out_degree'), 20)
    p = sorted_out_degrees.page(page).object_list
    p = list(map(lambda a: a.id, p))
    return HttpResponse(json.dumps(p))

def coef(request, page):
    sorted_coef = Paginator(Blog.objects.order_by('-coeffition'), 20)
    p = sorted_coef.page(page).object_list
    p = list(map(lambda a: a.id, p))
    return HttpResponse(json.dumps(p))

def reaching(request, page):
    sorted_reaching = Paginator(Blog.objects.order_by('-reaching_count'), 20)
    p = sorted_reaching.page(page).object_list
    p = list(map(lambda a: a.id, p))
    return HttpResponse(json.dumps(p))

def blog(request, blog):
    try:
        b = Blog.objects.filter(name=blog)[0]
    except:
        b = Blog()
        b.name = blog
        b.crawl_status = 'N'
        b.save()
        b.crawl()

    b.find_post()

    c = []
    for str in b.post.all()[0].get_text():
        c.append(str)

    context = {
        'blog': b,
        'contents': c,
    }

    return render(request, 'crawl/blog.html', context)

def link_count(request):
    counts = []
    for blog in Blog.objects.all():
        counts.append((len(Link.objects.filter(dest=blog)), blog.name))
    counts.sort()
    return HttpResponse(str(counts))

def fill_degrees():
    count = 0
    for blog in Blog.objects.all():
        if count % 100 == 0:
            print(count)
        count += 1
        blog.in_degree = blog.in_degree_count()
        blog.out_degree = blog.out_degree_count()
        blog.save()

def fill_coef():
    count = 0
    for blog in Blog.objects.all():
        if count % 100 == 0:
            print(count)

        count += 1
        blog.calc_coef()

def fill_reaching():
    count = 0
    for blog in Blog.objects.all():
        if count % 100 == 0:
            print(count)
        count += 1
        blog.calc_reaching()