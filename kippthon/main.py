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
import os
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
 -----------------------------------------------------
|                                                     |
|                     Kippt CLI                       |
|                                                     |
| @see      https://kippt.com/api/                    |
| @repo     https://github.com/nerdfiles/kippthon/    |
| @help     $ kippt [--help|-h]                       |
| @version  $ kippt [--version|-v]                    |
|                                                     |
 -----------------------------------------------------
'''
  sys.exit(1)


# == KIPPT POST ================================ #
#
# @date         08-12-2012
# @author       nerdfiles
#
# @param        url (expects urls)
# 
# @usage
# 
# $ kippt up:[url]

if 'up:' in u[0] and l:
  u = u[0].replace('up:', '')
  u = u.replace(' ', '+')
  
  if q[0] == '':
    print 'Forgot already?'
    sys.exit(1)
    
  os.system('curl --user ' + USER + ':' + PASSWORD + ' -X POST --data \'{"url": "' + u + '", "list": "/api/lists/1/"}\' https://kippt.com/api/clips/')
  # curl --user :password -X POST --data '{"url": "https://kippt.com", "list": "/api/lists/12/"}' https://kippt.com/api/clips/ 
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
  print search_cli(limit=l[0], q=q)
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
    print search_cli(limit=10, q=q)
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
  print lists_cli(l[0])
  sys.exit(1)

if 'lists' in u[0]:
  print lists_cli()
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
 -----------------------------------------------------
|                                                     |
|                    Kippt CLI Help                   |
|                                                     |
| Lists usage examples                                |
| ---------------------                               |
|                                                     |
| 1. $ kippt lists                                    |
| 2. $ kippt lists 5                                  |
|                                                     |
| Search usage examples                               |
| ---------------------                               |
|                                                     |
| 1. $ kippt search:'something phrase'                |
| 2. $ kippt search:"another phrase"                  |
| 3. $ kippt search:another+phrase                    |
| 4. $ kippt search:"something many" 10               |
|                                                     |
 -----------------------------------------------------
'''
  sys.exit(1)


