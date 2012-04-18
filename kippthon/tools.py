import pycurl
from pprint import pprint
import simplejson
import cStringIO
import urllib
import urllib2
from urllib2 import *
import sys
import re

# == LOCAL ======================================= #

try:
  from local_settings import *
except ImportError:
  pass

# == SEARCH ======================================= #
#
# For searching bookmarks.
#
# USAGE:
# 
# $ kippt search:python+cms 2

def search(limit='5', q=''):
  url = 'https://kippt.com/api/search/clips/?limit=%s&q=%s' % (limit, q,)
  req = urllib2.Request(url=url)
  req.add_header('X-Kippt-Username', USER)
  req.add_header('X-Kippt-API-Token', API_KEY)
  obj = None
  try:
    r = urllib2.urlopen(req)
    obj = simplejson.loads(r.read())
    if len(sys.argv) > 2:
      print '\nYour search query: %s' % sys.argv[2]
      print '------\n'
    if obj is not None:
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
  except URLError, e:
    print 'URL: %s' % e.url
    if hasattr(e, 'reason'):
      print 'ERROR: Could not reach server.'
      print e.reason
    elif hasattr(e, 'code'):
      print 'ERROR: Could not fulfill request.'
      print 'DETAILS: %s (%s)' % (e.msg, e.code,)

# == LIST ======================================= #
#
# Default behavior. 
# 
# USAGE:
# 
# $ kippt

def lists(limit=10):
  url = 'https://kippt.com/api/clips/?offset=0&limit='+str(limit)
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
      print '''%s:
%s. %s :: Note: %s''' % (item['list'], (idx+1), item['title'], item['notes'],)
    else:
      print '''%s:
%s. %s''' % (item['list'], (idx+1), item['title'],)
    print '%s' % item['url']
    if (idx+1) < len(obj['objects']):
      print '------\n'
    else:
      print '\n'
