import json
import requests as rq

api_uri='http://saidinosecondapp.herokuapp.com/spar/postproduct/'

def send_notification(message,title,image,to='/topics/ADMIN'):
    data={
        'to':'/topics/ADMIN',
        'body': message,
        'title':title',
        'image': image,
                }
    try:
        rq.post(api_uri,data=json.dumps(data))


print(resp.json)
