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
  q = sys.argv[1]
  p = re.compile('search\:')
  m = p.match(q, 0)
  l = sys.argv[2]

  # grab "search:" text
  #
  # @idea consider names: as interfaces to webapp/urls
  # @example $ merch:   # looks in a particular app or network of apps

  if q.startswith('search:'):
    q = q.replace('search:', '')
    q = q.replace(' ', '+')
    num = int(l)
    print '' + str(num) + ' results coming up...'
    print '------'
    search(limit=l, q=q)
    sys.exit(1)

if len(sys.argv) > 1:
  q = sys.argv[1]
  if q.startswith('search:'):
    q = q.replace('search:','')
    q = q.replace(' ', '+')
    search(limit=10, q=q)
    sys.exit(1)

# lists
# @usage 
# $ kippt lists 

if len(sys.argv) > 2:

  print 'Warily not, pity...'

  u = sys.argv[1] # @assume 'lists'
  l = sys.argv[2] # limit

  if u == 'lists' and l:
    lists(l)
    sys.exit(1)

if len(sys.argv) > 1:
  u = sys.argv[1]
  if u == 'lists':
    lists()

#if not m:
args = sys.argv
if len(args) < 2:
  print 'usage: [--todir dir] logfile '
  sys.exit(1)

