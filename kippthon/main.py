#!/usr/bin/env python

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
from tools import *
import config
# buf = cStringIO.StringIO()

# == LOCAL ===================================== #

try:
  from local_settings import *
except ImportError:
  pass


# == ARGS ====================================== #

args = sys.argv
u = sys.argv[1:] # @assume 'lists'
l = sys.argv[2:] # limit


# == KIPPT CLI ================================= #
# 
# @usage
#
# $ kippt

if not u:
  print 'Note: See --help for usage details.'
  sys.exit(1)


# == SEARCH ==================================== #
# 
# @usage
#
# $ kippt search:[query] [num]

# search with limit

if 'search:' in u[0] and l and int(l[0]) > 0:

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

# search

if 'search:' in u[0]:
  q = sys.argv[1]
  if q.startswith('search:'):
    q = q.replace('search:','')
    q = q.replace(' ', '+')
    if q == '':
      print 'For?'
      sys.exit(1)
    print search(limit=10, q=q)
    sys.exit(1)


# == LISTS ===================================== #
#
# @usage
#
# $ kippt lists [num]

if 'lists' in u[0] and l and l[0] > 0:
  print lists(l[0])
  sys.exit(1)

if 'lists' in u[0]:
  print lists()
  sys.exit(1)

# == VERSION =================================== #
#
# @usage
#
# $ kippt [--version|-v]

if '--version' in args or '-v' in args:
  print 'Kippt %s' % config.VERSION
  sys.exit(1)


# == HELP ====================================== #
#
# @usage
#
# $ kippt [--help|-h]

if '--help' in args or '-h' in args:
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


