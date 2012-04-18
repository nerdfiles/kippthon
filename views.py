# -*- coding: utf-8 -*-

from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
import sys
from kippthon.tools import *

def render_response(req, *args, **kwargs):
  kwargs['context_instance'] = RequestContext(req)
  return render_to_response(*args, **kwargs)

def kippt(self):
  print search(10, 'python')
  return render_response(self, '')
