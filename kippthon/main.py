#!/usr/bin/env python

import pycurl
from pprint import pprint
import simplejson
import cStringIO
import urllib
import urllib2
import sys

buf = cStringIO.StringIO()

USER = 'nerdfiles'


# == LOCAL ======================================= #

try:
  from local_settings import *
except ImportError:
  pass

def search(q=''):
  url = 'https://kippt.com/api/search/clips/?limit=5&q=%s' % q
  req = urllib2.Request(url=url)
  req.add_header('X-Kippt-Username', USER)
  req.add_header('X-Kippt-API-Token', API_KEY)
  r = urllib2.urlopen(req)
  obj = simplejson.loads(r.read())
  #pprint( obj )
  for item in obj['objects']:
    print item['title']

def lists():
  url = 'https://kippt.com/api/lists/?offset=0&limit=2'
  # provide @prop data for post
  req = urllib2.Request(url=url)
  req.add_header('X-Kippt-Username', USER)
  req.add_header('X-Kippt-API-Token', API_KEY)
  r = urllib2.urlopen(req)
  obj = simplejson.loads(r.read())
  pprint( obj )

if (len(sys.argv) > 1):
  search(q=sys.argv[1])
else:
  lists()


