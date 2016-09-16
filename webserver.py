#!/usr/bin/env python

from flask import Flask, render_template, session, request
import config
import requests
import json

app = Flask(__name__)
app.secret_key = config.secret_session_key

LATITUDE = 37.786882
LONGITUDE = -122.399972
YELP_ACCESS_TOKEN = "yelp_access_token"
EMPTY_RESPONSE = json.dumps('')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/business_search")
def business_search():
    term = request.args.get("term", None)
    if term == None:
        print "No term provided for business search, returning nothing"
        return EMPTY_RESPONSE

    response = requests.get('https://api.yelp.com/v3/businesses/search',
            params=get_search_params(term),
            headers=get_auth_dict(get_yelp_access_token()))
    if response.status_code == 200:
        print "Got 200 for business search"
        return json.dumps(response.json())
    else:
        print "Received non-200 response({}) for business search, returning empty response".format(response.status_code)
        return EMPTY_RESPONSE


@app.route("/autocomplete")
def autocomplete():
    term = request.args.get("term", None)
    if term==None:
        print "No term provided for autocomplete, returning nothing"
        return EMPTY_RESPONSE
    print "autocompleting for: ", term
    
    response = requests.get('https://api.yelp.com/v3/autocomplete', params=get_autocomplete_params(term), headers=get_auth_dict(get_yelp_access_token()))
    if response.status_code == 200:
        # We return a list of businesses that autocomplete appended with a list of terms that autocomplete.
        return json.dumps([business['name'] for business in response.json()['businesses']]
        + [term['text'] for term in response.json()['terms']])
    else:
        print "received non-200 response({}) for autocomplete, returning empty response".format(response.status_code)
        return EMPTY_RESPONSE


def get_yelp_access_token():
    # WARNING: Ideally we would also expire the token. An expiry is sent with the token which we ignore.
    if YELP_ACCESS_TOKEN in session:
        print "access token found in session"
    else:
        print "access token needs to be retrieved"
        response = requests.post('https://api.yelp.com/oauth2/token', data=config.yelp_api_auth)
        if response.status_code == 200:
            session[YELP_ACCESS_TOKEN] = response.json()['access_token']
            print "stored access token in session:", session[YELP_ACCESS_TOKEN]
        else:
            raise RuntimeError("Unable to get token, received status code " + str(response.response))
    
    return session[YELP_ACCESS_TOKEN]


def get_search_params(term, latitude=LATITUDE, longitude=LONGITUDE):
    return {'term': term, 'latitude' : latitude, 'longitude' : longitude}


def get_autocomplete_params(term, latitude=LATITUDE, longitude=LONGITUDE):
    return {'text': term, 'latitude' : latitude, 'longitude' : longitude}


def get_auth_dict(access_token):
    return {'Authorization' : "Bearer " + access_token}


if __name__ == "__main__":
    app.run()
