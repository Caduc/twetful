import urlparse
import requests
from requests_oauthlib import OAuth1

from secret import CLIENT_KEY, CLIENT_SECRET
from urls import *


def get_request_token():
    """ Get a token allowing us to request user authorization  """
    # First create instance of OAuth1 class and give this our client 
    # key and secret
    oauth = OAuth1(CLIENT_KEY, client_secret=CLIENT_SECRET)
    # Then we make a POST request to the request token endpoint passing 
    # in the oauth object as our credentials 
    response = requests.post(REQUEST_TOKEN_URL, auth=oauth)
    # We use the parse_qs function from the urlparse module to store
    # to create a dictionar with the request token and secret
    # (response.content contains the request token and secret in a query string)
    credentials = urlparse.parse_qs(response.content)
    # We use the dictionaries get method to retrieve the token and secret
    # and return them
    request_token = credentials.get("oauth_token")[0]
    request_secret = credentials.get("oauth_token_secret")[0]
    return request_token, request_secret

def get_user_authorization(request_token):
    '''
    Redirect the user to authorize the client, and get them a verification code
    '''
    authorize_url = AUTHORIZE_URL 
    authorize_url = authorize_url.format(request_token=request_token)
    print 'Please go hera and authorize: ' + authorize_url
    return raw_input('Please input the verifier: ')

def authorize():
    #A complete OAuth authentication flow
    request_token, request_secret = get_request_token()
    #print request_token, request_secret
    verifier = get_user_authorization(request_token)