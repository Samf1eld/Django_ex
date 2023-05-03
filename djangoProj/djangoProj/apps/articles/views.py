"""from django.http import HttpResponse

def index(request):
    return HttpResponse("Done! Check more later!")"""
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article
from django.urls import reverse
from django.utils import timezone

def index(request):
    latest_articles_list = Article.objects.order_by('-a_pub_dt')[:6]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Statements was not found")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article':a, 'latest_comments_list':latest_comments_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Statements was not found")

    a.comment_set.create(c_au_name=request.POST['name'], c_content=request.POST['text'])

    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )

def new_article(request):
    return HttpResponseRedirect( reverse('articles:new_article_detail', ))

def new_article_detail(request):
    try:
        time = timezone.now()
    except:
        raise Http404("Statements was not found")

    return render(request, 'articles/new_article_detail.html', {'curtime': time})

def new_article_create(request):
    Article.objects.create(a_title=request.POST['title'], a_content=request.POST['content'], a_pub_dt=timezone.now())

    return HttpResponseRedirect( reverse('articles:index', ))
