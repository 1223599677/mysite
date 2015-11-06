#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-05 15:16:51
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
