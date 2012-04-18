# -*- coding: utf-8 -*-

from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
import sys
from kippthon.funcs import *

def render_response(req, *args, **kwargs):
  kwargs['context_instance'] = RequestContext(req)
  return render_to_response(*args, **kwargs)

'''
  @usage 
    http://localhost:8000/kippt/lists/
    http://localhost:8000/kippt/lists/20/
'''

def lists(self, limit=None):
  if limit == None:
    limit = 10
  l = kippt_lists(limit)
  return render_response(self, 'base.tmpl', { 'results': l})

'''
  @usage 
    http://localhost/kippt/search/content+management+systems/
    http://localhost/kippt/search/python+django/20/
'''

def search(self, q, limit=None):
  if limit == None:
    limit = 10
  r = kippt_search(limit, q)
  return render_response(self, 'base.tmpl', { 'results': r})
