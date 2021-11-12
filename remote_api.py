import json
import requests as rq

# api_uri='http://saidinosecondapp.herokuapp.com/spar/postproduct/'
api_uri='http://localhost:5000/spar/postproduct/'

def send_notification(message,title,image,to='/topics/ADMIN'):
    data={
        'to':'/topics/ADMIN',
        'body': message,
        'title':title,
        'image': image,
                }
    try:
        resp=rq.post(api_uri,json=json.dumps(data))
        print(resp.text)
    except  Exception as e:
        print(e)
image='https://vipspar.com/wp-content/uploads/2020/07/38145-480x480.jpg'
send_notification(message="The message",title="title",image=image)