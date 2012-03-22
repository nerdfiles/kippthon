import pycurl
from pprint import pprint
import simplejson
import cStringIO
import urllib
import urllib2

buf = cStringIO.StringIO()

USER = 'nerdfiles'
API_KEY = 'cb08721433031016984ebc269e4f07e0a1d8ce4b'

def kippt():
  url = 'https://kippt.com/api/lists/'
  # provide @prop data for post
  req = urllib2.Request(url=url)
  req.add_header('X-Kippt-Username', USER)
  req.add_header('X-Kippt-API-Token', API_KEY)
  r = urllib2.urlopen(req)
  obj = simplejson.loads(r.read())
