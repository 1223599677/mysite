#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-05 13:59:54
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com

try:
    from django.contrib.sites.models import get_current_site
except ImportError:
    from django.contrib.sites.shortcuts import get_current_site

from django.conf import settings as project_settings

from users.models import User
from utils.models import VisitRecord


def common(request):
    site = get_current_site(request)

    return {
        'settings': project_settings,
        'site_name': site.name,
        'protocol': 'https' if request.is_secure() else 'http',
        'domain': site.domain,
        'site': site,

        'user_count': User.objects.count(),
        'visit_count': VisitRecord.objects.count(),
        # VisitRecord.objects.all().order_by('-create_time')[0].id

        'ip_address': request.META['REMOTE_ADDR'],
    }
