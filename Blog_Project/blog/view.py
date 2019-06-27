from django.shortcuts import render
import logging
from django.conf import settings

logger = logging.getLogger('blog.views')

def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_DESC': settings.SITE_DESC}

def index(request):
    try:
        return render(request, 'index.html', locals())
    except Exception as e:
        logger.error(e)
    