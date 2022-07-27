from flask import render_template, url_for, request, redirect, Blueprint, jsonify, flash
import requests
import sys #print(..., file=sys.stderr)
from ..models import UserModel
import json

BASE = "http://127.0.0.1:5000/"
LOCATIONURL = BASE + "location"
LOCATIONLISTURL = BASE + "locationlist"
GEONAMEURL = BASE + 'geoname'
views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = LOCATIONURL
        # first_name = request.form.get('first-name') #form in html input has name of content
        # last_name = request.form.get('last-name')
        email = request.form.get('email')
        city = request.form.get('city')
        country = request.form.get('country')
        geo_name_response = _get_location_info(city)
        lat = geo_name_response['lat']
        lng = geo_name_response['lng']
        if len(city) <= 0:
            flash("City can't be empty" , "warning")
            return redirect(url_for('views.index'))
        body = {'email': email,
                'city': city,
                'country': country,
                'lng': lng,
                'lat': lat}
        try:
            response = requests.post(url, body)
            new_user = response.json()
            print("HERE3", file=sys.stderr)
            print(new_user, file=sys.stderr)
            flash("Location added!" , "success")
            return redirect(url_for('views.index'))
        except:
            return "There was an issue adding your location"

    else:
        response = requests.get(LOCATIONLISTURL)
        users = response.json()
        print(users, file=sys.stderr)
        return render_template("index.html", users = users)

def _get_location_info(city):
    url = GEONAMEURL + f'/{city}'
    response = requests.get(url)
    print("HERE", file=sys.stderr)
    print(response, file=sys.stderr)
    print(response.json(), file=sys.stderr)
    return response.json()
