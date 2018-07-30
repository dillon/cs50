import os
import re
from flask import Flask, jsonify, render_template, request

from cs50 import SQL
from helpers import lookup

# Configure application
app = Flask(__name__)

# config
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///mashup.db")

# function to see see if value is an int


def tryer(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Render map"""
    return render_template("index.html")


@app.route("/articles")
def articles():
    """Look up articles for geo"""
    geo = request.args.get("geo")
    if not geo:
        raise RuntimeError("no results from request.args.get(\"geo\")")
    results = lookup(geo)
    # lookup(geo) returns array of [{"link": item["link"], "title": item["title"]} for item in feed["items"]]
    if not results:
        raise RuntimeError("no results from lookup(geo)")
    return jsonify(results)


@app.route("/search")
def search():
    """Search for places that match query"""
    q = request.args.get("q") + "%"
    # if first char is an int, just look at postal codes
    if(tryer(q[0])):
        results = db.execute("""
            SELECT * FROM places
            WHERE postal_code LIKE :q
            LIMIT :i
        """,
                             q=q,
                             i=4
                             )
    # if first char isn't an int, just look at places and states
    else:
        results = (db.execute("""
            SELECT * FROM places
            WHERE place_name LIKE :q
            LIMIT :i
        """,
                              q=q,
                              i=4
                              )
                   )
    if len(results) < 4:
        results.extend(db.execute("""
            SELECT * FROM places
            WHERE admin_name1 LIKE :q
            LIMIT :i
        """,
                                  q=q,
                                  i=4 - len(results)
                                  )
                       )

    return jsonify(results)


@app.route("/update")
def update():
    """Find up to 10 places within view"""

    # Ensure parameters are present
    if not request.args.get("sw"):
        raise RuntimeError("missing sw")
    if not request.args.get("ne"):
        raise RuntimeError("missing ne")

    # Ensure parameters are in lat,lng format
    if not re.search("^-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?$", request.args.get("sw")):
        raise RuntimeError("invalid sw")
    if not re.search("^-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?$", request.args.get("ne")):
        raise RuntimeError("invalid ne")

    # Explode southwest corner into two variables
    sw_lat, sw_lng = map(float, request.args.get("sw").split(","))

    # Explode northeast corner into two variables
    ne_lat, ne_lng = map(float, request.args.get("ne").split(","))

    # Find 10 cities within view, pseudorandomly chosen if more within view
    if sw_lng <= ne_lng:

        # Doesn't cross the antimeridian
        rows = db.execute("""SELECT * FROM places
                          WHERE :sw_lat <= latitude AND latitude <= :ne_lat AND (:sw_lng <= longitude AND longitude <= :ne_lng)
                          GROUP BY country_code, place_name, admin_code1
                          ORDER BY RANDOM()
                          LIMIT 10""",
                          sw_lat=sw_lat, ne_lat=ne_lat, sw_lng=sw_lng, ne_lng=ne_lng)

    else:

        # Crosses the antimeridian
        rows = db.execute("""SELECT * FROM places
                          WHERE :sw_lat <= latitude AND latitude <= :ne_lat AND (:sw_lng <= longitude OR longitude <= :ne_lng)
                          GROUP BY country_code, place_name, admin_code1
                          ORDER BY RANDOM()
                          LIMIT 10""",
                          sw_lat=sw_lat, ne_lat=ne_lat, sw_lng=sw_lng, ne_lng=ne_lng)

    # Output places as JSON
    return jsonify(rows)
