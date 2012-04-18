#!/usr/bin/env python

# == IMPORTS ======================================= #

import pycurl
from pprint import pprint
import simplejson
import cStringIO
import urllib
import urllib2
from urllib2 import *
import sys
import re
from tools import *
# buf = cStringIO.StringIO()

# == LOCAL ======================================= #

try:
  from local_settings import *
except ImportError:
  pass

# == SEARCH ====================================== #
#
# @usage 
# 
# $ kippt search:some+thought+of+yours
#

m = ''

if len(sys.argv) > 2:
  q = sys.argv[1:]
  #p = re.compile('search\:')
  #m = p.match(q, 0)
  l = sys.argv[2:]

  # grab "search:" text
  #
  # @idea consider names: as interfaces to webapp/urls
  # @example $ merch:   # looks in a particular app or network of apps

  if 'search' in q[0]:
    q = q[0].replace('search:', '')

    if q == '':
      print 'For?'
      sys.exit(1)

    q = q.replace(' ', '+')
    num = int(l[0])
    print '' + str(num) + ' results coming up...'
    print '------'
    print search(limit=l[0], q=q)
    sys.exit(1)

if len(sys.argv) > 1:
  q = sys.argv[1]
  if q.startswith('search:'):
    q = q.replace('search:','')
    q = q.replace(' ', '+')
    if q == '':
      print 'For?'
      sys.exit(1)
    print search(limit=10, q=q)
    sys.exit(1)

# lists
# @usage 
# $ kippt lists [num]

if len(sys.argv) > 2:

  print 'Warily not, pity...'

  u = sys.argv[1:] # @assume 'lists'
  l = sys.argv[2:] # limit
  l = int(l[0])
  if 'lists' in u and l > 0:
    print lists(l)
    sys.exit(1)

# lists
# @usage
# $ kippt lists

if len(sys.argv) > 1:
  u = sys.argv[1:]
  if 'lists' in u:
    print lists()
    sys.exit(1)

#if not m:
args = sys.argv
if len(args) < 2:
  print ''' 
 -------------------------------------------------------------
|                                                             |
| Kippt CLI (https://kippt.com/api/)                          |
|                                                             |
| Print most recent saves to Kippt                            |
|                                                             |
| $ kippt lists                                               |
|                                                             |
| Print most recent saves to Kippt and limit result set       |
|                                                             |
| $ kippt lists 5                                             |
|                                                             |
| Search phrase                                               |
|                                                             |
| $ kippt search:"something phrase"                           |
|                                                             |
| or (with double quotes):                                    |
|                                                             |
| $ kippt search:"another phrase"                             |
|                                                             |
| Search phrase and limit result set                          |
|                                                             |
| $ kippt search:"something many" 10                          |
|                                                             |
 --------------------------------------------------------------'''
  sys.exit(1)

