```python
import json
import requests as rq

api_uri='http://localhost:5000/spar/postproduct/'
auth='key=AAAAT7I801w:APA91bFyk0q5leLPRR8YtKy3Q1s1wA38IcLdhZbkXF3ysCY7HdwOZ2IJEMQoaO8t5zKTwE_A8hockdmrL1FgkKkbqfK6FX4eCP5R7o1XLliD-e3OYFY1aruXPxac9rc_x6Dr6ly17nER'

fcm_uri='https://fcm.googleapis.com/fcm/send'
headers ={
        'Content-Type': 'application/json', 'Authorization': auth,
        }
body={
            'to':'/topics/ADMIN',
            'notification':{
            'message': 'Hi from flask it comes from',
            'title':'The flask title',
            'image_url':'https://e7.pngegg.com/pngimages/798/40/png-clipart-pomegranate-fruit-juice-pomegranate-fruit-food-pomegranate-fruit-natural-foods-frutti-di-bosco.png',}}
resp=rq.post(fcm_uri,headers=headers,data=json.dumps(body))

print(resp.content)

```
