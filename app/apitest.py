import unittest
import requests
import sys #print(..., file=sys.stderr)



class ApiTest (unittest.TestCase):
    BASE = "http://127.0.0.1:5000/"
    LOCATIONURL = BASE + "user"
    LOCATIONLISTURL = BASE + "userlist"
    USER_OBJ = {
        'id' :1 ,
        'email': 'Jonathan@gmail.com',
        'city'  :'Irvine',
        'country': 'United States',
        'lat'   : '100',
        'lng'   : '150'
    }

    def _get_each_user_url(self,id):
        return f'{ApiTest.LOCATIONURL}/{id}'

    #POST request to /todo to create a new todo
    def test_1_add_new_task(self):
        response = requests.post(ApiTest.LOCATIONURL, json = ApiTest.USER_OBJ)
        self.assertEqual(response.status_code,201)

    #GET request to test new task is added
    def test_2_get_new_task(self):
        id = ApiTest.USER_OBJ['id']
        response = requests.get(self._get_each_user_url(id))
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), ApiTest.USER_OBJ)


        

    



