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

  kippt search cli

  search for kippt bookmarks

  @date     04-17-2012
  @author   nerdfiles

'''

def search_cli(limit=10, q=''):
  url = 'https://kippt.com/api/search/clips/?limit=%s&q=%s' % (str(limit), q,)
  req = urllib2.Request(url=url)
  req.add_header('X-Kippt-Username', USER)
  req.add_header('X-Kippt-API-Token', API_KEY)
  obj = None
  o = ''
  try:
    r = urllib2.urlopen(req)
    obj = simplejson.loads(r.read())
    if q != '':
      o += '\nYour search query: %s' % q
      o += '\n\n------\n\n'
    if obj is not None:
      for idx, item in enumerate(obj['objects']):
        if item['notes']:
          o += '%s. %s :: Note: %s' % ((idx+1), item['title'], item['notes'],)
        else:
          o += '%s. %s' % ((idx+1), item['title'],)
        o += '\n[%s]' % item['url']
        if (idx+1) < len(obj['objects']):
          o += '\n\n------\n\n'
        else:
          o += '\n'
    return o 
  except URLError, e:
    o += 'URL: %s' % e.url
    if hasattr(e, 'reason'):
      o += 'ERROR: Could not reach server.'
      o += e.reason
    elif hasattr(e, 'code'):
      o += 'ERROR: Could not fulfill request.'
      o += 'DETAILS: %s (%s)' % (e.msg, e.code,)


'''

  kippt lists cli

  print lists from kippt

  @date 04-17-2012
  @author nerdfiles 

'''

def lists_cli(limit=10):
  url = 'https://kippt.com/api/clips/?offset=0&limit=%s' % str(limit)
  # provide @prop data for post
  req = urllib2.Request(url=url)
  req.add_header('X-Kippt-Username', USER)
  req.add_header('X-Kippt-API-Token', API_KEY)
  r = urllib2.urlopen(req)
  obj = simplejson.loads(r.read())
  #pprint( obj )
  o = '\n'
  for idx, item in enumerate(obj['objects']):
    if item['notes']:
      o += '''%s:
%s. %s :: Note: %s''' % (item['list'], (idx+1), item['title'], item['notes'],)
    else:
      o += '''%s: 
%s. %s''' % (item['list'], (idx+1), item['title'],)
    o += '\n[%s]' % item['url']
    if (idx+1) < len(obj['objects']):
      o += '\n\n------\n\n'
    else:
      o += '\n'
  return o
