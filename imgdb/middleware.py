#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-05 16:11:05
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com

from utils.models import VisitRecord


class StatisticsMiddleware(object):
    def process_request(self, request):
        counted_user = request.session.get('counted_user', default=None)
        if counted_user is None:
            # create a new visit record
            VisitRecord.objects.create()

            request.session.set_expiry(600)
            request.session['counted_user'] = 1

        return None

    def process_response(self, request, response):
        return response
