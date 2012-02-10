import pycurl

def auth():
  c = pycurl.Curl()
  c.setopt(c.URL, 'https://kippt.com/api/v0/')
  c.setopt(c.POSTFIELDS, 'username=nerdfiles&api_key=' + API_KEY)
  c.perform()

def kippt():
  c = pycurl.Curl()
  c.setopt(c.URL, '')
  c.perform()
