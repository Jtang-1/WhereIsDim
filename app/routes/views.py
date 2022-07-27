from flask import render_template, url_for, request, redirect, Blueprint, flash
import requests
import sys #print(..., file=sys.stderr)

BASE = "http://127.0.0.1:5000/"
LOCATIONURL = BASE + "user"
LOCATIONLISTURL = BASE + "userlist"
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
            flash("Location added!" , "success")
            return redirect(url_for('views.index'))
        except:
            return "There was an issue adding your location"

    else:
        response = requests.get(LOCATIONLISTURL)
        users = response.json()
        return render_template("index.html", users = users)

def _get_location_info(city):
    url = GEONAMEURL + f'/{city}'
    response = requests.get(url)
    return response.json()
