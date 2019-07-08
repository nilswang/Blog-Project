#! /usr/bin/env python3
#-*- coding: utf8 -*-


from django.shortcuts import render
import logging
from django.conf import settings
from blog.models import *
from django.db.models import Count
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
logger = logging.getLogger('blog.views')

def global_setting(request):
    site_name = settings.SITE_NAME
    site_desc = settings.SITE_DESC
    category_list = Category.objects.all()
    archive_list = Article.objects.distinct_date()
    ad_list = Ad.objects.all()
    comment_conut_list = Comment.objects.values('article').annotate(commentcount=Count('article')).order_by('-commentcount')
    print(comment_conut_list)

    article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_conut_list]
    return locals()
    #{'category_list': category_list,
            #'archive_list': archive_list,
            #'SITE_NAME': settings.SITE_NAME,
            #'SITE_DESC': settings.SITE_DESC,
            #'ad_list':ad_list}

def index(request):
    try:
        #分类信息获取
        #广告数据
        #最新文章数据
        article_list = getPage(request, Article.objects.all())
    except Exception as e:
        print(e)
        logger.error(e)
    return render(request, 'index.html', locals())

def archive(request):
    try:
        # 先获取用户提交的year和month信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        # 通过filter过滤出对应年份的数据（icontains是包含）
        article_list = getPage(request, Article.objects.filter(date_publish__icontains=year + '-' + month))
    except Exception as e:
        logging.error(e)
    return render(request, 'archive.html', locals())

def getPage(request, article_list):
    paginator = Paginator(article_list, 1)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list