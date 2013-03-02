# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:34:59 2013

@author: koosha
"""

from django.shortcuts import render_to_response

def home_page(request):
    return render_to_response('Father_temp.html',locals())