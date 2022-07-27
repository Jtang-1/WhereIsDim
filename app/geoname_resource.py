from . import db
from flask_restful import Resource, fields
import requests
import sys #print(..., file=sys.stderr)
import urllib

BASE = 'http://api.geonames.org/searchJSON?'
USERNAME = 'dimagi'



class GeonameApiResource(Resource):
    #handles getting(get), updating(put), & deleting (del)  individual tasks
    def get(self, city):
        query = {'q': city, 'username': USERNAME}
        encoded = urllib.parse.urlencode(query)
        response = requests.get(BASE + encoded)
        geo_data = response.json()['geonames'][0]
        body = {
            'lng'   : geo_data['lng'],
            'lat'   :  geo_data['lat'],
            'city_name' : geo_data['toponymName'],
            'country_name'  : geo_data['countryName']
        }
    
        return body,200

