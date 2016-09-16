# Copy as "config.py" and insert your Yelp credentials. See README.md for details.

yelp_api_auth = {
    'client_id' : '<CLIENT_ID>',
    'client_secret' : '<CLIENT_SECRET>',
    'grant_type' : 'client_credentials'
}

# Create a secret session key for Flask. Easy to do in python:
# import os
# os.urandom(24)
secret_session_key = '<GENERATE RANDOM KEY>'
