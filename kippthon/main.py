#!/usr/bin/env python

import pycurl
from pprint import pprint
import simplejson
import cStringIO
import urllib
import urllib2
import sys
import re

buf = cStringIO.StringIO()

USER = 'nerdfiles'


# == LOCAL ======================================= #

try:
  from local_settings import *
except ImportError:
  pass

def search(limit='5', q=''):
  url = 'https://kippt.com/api/search/clips/?limit=%s&q=%s' % (limit, q,)
  req = urllib2.Request(url=url)
  req.add_header('X-Kippt-Username', USER)
  req.add_header('X-Kippt-API-Token', API_KEY)
  r = urllib2.urlopen(req)
  obj = simplejson.loads(r.read())
  print '\nYour search query: %s' % sys.argv[2]
  print '------\n'
  for idx, item in enumerate(obj['objects']):
    if item['notes']:
      print '%s. %s :: Note: %s' % ((idx+1), item['title'], item['notes'],)
    else:
      print '%s. %s' % ((idx+1), item['title'],)
    print '%s' % item['url']
    if (idx+1) < len(obj['objects']):
      print '------\n'
    else:
      print '\n'

def lists():
  url = 'https://kippt.com/api/clips/?offset=0&limit=10'
  # provide @prop data for post
  req = urllib2.Request(url=url)
  req.add_header('X-Kippt-Username', USER)
  req.add_header('X-Kippt-API-Token', API_KEY)
  r = urllib2.urlopen(req)
  obj = simplejson.loads(r.read())
  #pprint( obj )
  print '\n'
  for idx, item in enumerate(obj['objects']):
    if item['notes']:
      print '%s. %s :: Note: %s' % ((idx+1), item['title'], item['notes'],)
    else:
      print '%s. %s' % ((idx+1), item['title'],)
    print '%s' % item['url']
    if (idx+1) < len(obj['objects']):
      print '------\n'
    else:
      print '\n'

m = ''

# bash no trim

if len(sys.argv) > 1:
  q = sys.argv[1]
  p = re.compile("search\:")
  m = p.match(q, 0)
  q = q.replace("search:", "")
  search(limit=sys.argv[2], q=q)

if not m:
  lists()

'''
  USAGE

  1. kippt search:python+cms 2
  2. kippt
'''



