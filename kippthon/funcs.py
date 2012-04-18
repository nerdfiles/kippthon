# -*- coding: utf-8 -*-

# == IMPORTS =================================== #

import pycurl
from pprint import pprint
import simplejson
import cStringIO
import urllib
import urllib2
from urllib2 import *
import sys
import re

# == LOCAL ===================================== #

try:
  from local_settings import *
except ImportError:
  pass


# == TOOLS ===================================== #

''' 

  kippt search

  search for kippt bookmarks

  @date     04-17-2012
  @author   nerdfiles

'''

def kippt_search(limit=10, q=''):
  url = 'https://kippt.com/api/search/clips/?limit=%s&q=%s' % (str(limit), q,)
  req = urllib2.Request(url=url)
  req.add_header('X-Kippt-Username', USER)
  req.add_header('X-Kippt-API-Token', API_KEY)
  obj = None
  o = ''
  try:
    r = urllib2.urlopen(req)
    obj = simplejson.loads(r.read())
    return obj
  except URLError, e:
    return e


'''

  kippt lists cli

  print lists from kippt

  @date 04-17-2012
  @author nerdfiles 

'''

def kippt_lists(limit=10):
  url = 'https://kippt.com/api/clips/?offset=0&limit=%s' % str(limit)
  # provide @prop data for post
  req = urllib2.Request(url=url)
  req.add_header('X-Kippt-Username', USER)
  req.add_header('X-Kippt-API-Token', API_KEY)
  try:
    r = urllib2.urlopen(req)
    obj = simplejson.loads(r.read())
    return obj
  except URLError, e:
    return e
