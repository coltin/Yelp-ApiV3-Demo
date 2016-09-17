# Yelp APIv3 Demo

A simple Flask app to demo Yelps API to autocomplete and search for businesses.

# Usage

To run this demo you have to have Python 2.7 and pip. You also need to install Flask and requests:
pip install Flask
pip install requests

**TODO:** Use pythons concept of requirements.

Copy "config-replace.py" to "config.py" and follow the instructions in this file. You want to replace the client id and client secret with your Yelp API V3 credentials.

You then need to run the web server.

**./webserver.py**

This will spin up the web server which can be accessed over localhost on port 5000.


# FAQ
**Why python 2.7?**

At this time, a requirement of Flask.

**Why Flask?**

It was the first thing I found.

**Learn more about Yelp API v3?**

https://github.com/Yelp/yelp-api-v3/blob/master/docs/tutorials/get-start-yelp-api-v3.md
