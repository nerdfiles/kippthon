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

# search
# @usage 
# 
# $ kippt search:some+thought+of+yours
#

m = ''

if len(sys.argv) == 3:
  q = sys.argv[1]
  p = re.compile('search\:')
  m = p.match(q, 0)
  q = q.replace('search:', '')
  num = sys.argv[2]
  if num:
    num = int(sys.argv[2])
    print '' + str(num) + ' results coming up...'
    print '------'
    search(limit=sys.argv[2], q=q)
  lists()
  sys.exit(1)

# lists
# @usage 
# $ kippt lists 

if len(sys.argv) == 2:

  print 'Warily not, pity...'

  q = sys.argv[1]

  if q == 'lists':
    lists()

  sys.exit(1)

#if not m:
args = sys.argv
if not args:
  print 'usage: [--todir dir] logfile '
  sys.exit(1)

