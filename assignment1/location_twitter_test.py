import oauth2 as oauth
import urllib2 as urllib
import sys
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = "g0qzK8JjEjGlmMDepLZrUU6CL"
api_secret = "aBwgGAxBHFPO6MnDsQJ2f8ZYH6fMyHA9m9u3mtWrQ8KdKlFiW9"
access_token_key = "23799954-o394XpQMtfEiAZ3zWqWUAIFHgl8Vl3lNRqEC7dlSc"
access_token_secret = "qqRghb9Ci7dHLjQlot62KuTrlhoRh0rLWrU3JZYntO4hU"

_debug = 0



oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  #url = "https://api.twitter.com/1.1/search/tweets.json?q=feel"
  url = "https://api.twitter.com/1.1/search/tweets.json?geocode=-27.600249,-48.520316,10km"
  #url = "https://api.twitter.com/1.1/geo/search.json?query=AntiMachismoNerd"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  #for line in response:
  #  print line.strip()

  for line in response:
  		jsonline = json.loads(line)

  
  for i in range(0,len(jsonline["statuses"])):
  	print "\n"
  	print jsonline["statuses"][i]["user"]["screen_name"]
  	print jsonline["statuses"][i]["coordinates"]
  	print jsonline["statuses"][i]["text"].encode('utf-8')

if __name__ == '__main__':
  fetchsamples()
