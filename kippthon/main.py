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
# Call Kippt.
#
# @date         04-17-2012
# @author       nerdfiles
#
# @usage
#
# $ kippt

if not u:
  print '''
# ============================================== #
#                                                #
#                   Kippt CLI                    #
#                                                #
# @see      https://kippt.com/api/               #
# @help     $ kippt [--help|-h]                  #
# @version  $ kippt [--version|-v]               #
#                                                #
# ============================================== #
'''
  sys.exit(1)


# == KIPPT SEARCH ============================== #
# 
# Search your bookmarks.
#
# @date         04-17-2012
# @author       nerdfiles
#
# @param        query (expects string; e.g., 'some string', "some string", some+string)
# @param        num (expects int; e.g., 5)
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

  q = u[0].replace('search:', '')
  q = q.replace(' ', '+')
  num = int(l[0])

  if q[0] == '':
    print 'For?'
    sys.exit(1)

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
# @date         04-17-2012
# @author       nerdfiles
#
# @param        num (expects int; e.g., 20)
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
# @date         04-17-2012
# @author       nerdfiles
#
# @usage
#
# $ kippt [--version|-v]

if '--version' in args or '-v' in args:
  print 'Kippt %s' % config.VERSION
  sys.exit(1)


# == HELP ====================================== #
#
# @date         04-17-2012
# @author       nerdfiles
#
# @usage
#
# $ kippt [--help|-h]

if '--help' in args or '-h' in args:
  print ''' 
# Kippt CLI Help

## Print most recent saves to Kippt
---
$ kippt lists

## Print most recent saves to Kippt and limit result set
---
$ kippt lists 5

## Search phrase
---
$ kippt search:'something phrase'

## Or (with double quotes):
---
$ kippt search:"another phrase"

## Or:
---
$ kippt search:another+phrase

## Search phrase and limit result set
---
$ kippt search:"something many" 10

'''
  sys.exit(1)


