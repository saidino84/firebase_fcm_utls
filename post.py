
import json
import requests as rq

# server uri
fcm_server='https://fcm.googleapis.com/fcm/send'
# [headers]
auth='key=AAAAQFHnrVQ:APA91bEFAGGIr7pOVAm3g2sNQZfvI9ZlCuQtYq0Toy-gHqEYlA_wybPGls9wrjcoW7FNoyXRqmZi2l5CavXSbxn-yfMkakVba1PaacxJ0REnoYiBMj7DMezx9dKDpitefB0F652V7vy7'
content_type='application/json'
headers={
    'Content-Type':'application/json',
    'Authorization':auth
}

# USERS
wife='ePbRZsCgTDuHwVhHbTsEGT:APA91bGJY2xrgKlMnD7Inf95jjPBc404sTK2nfh4fqb_HEWzHvgOCHrzYV-K_Hu68X0941kx_1coFUQcl9xfRaShZhmha6lMixGnXXFOjkWN8NG8L6z6msrj2I5f8Kk1m7HOcE0lQUNV'
mine="dA8SJnyqSGGF5s6mWJ_wp2:APA91bHInq0DgMVL5usx_zCiJXwapXLioqOXnAoGd9Df3WoFyAQEB0bfFqWX-KiQ2FmXbmMhIAjAXuUkTEPZxe8zPwfJPrRiWG55CV0BEKnG_urbNCfAmCf_y8RA-p4NT56hIWudOeRU"
# [body]
message=input('message')
title =input('title')
image_url=input('image link')
if(len(image_url) <10):
    image_url='https://st.depositphotos.com/1063437/2337/i/950/depositphotos_23373292-stock-photo-groceries-in-wicker-basket-including.jpg'
body={
    "to":wife,
    "notification":{
        "body":message,
        "title":title,
        "image":image_url
        
    },
    "data":{
        "body":"Body :Data",
        "title":"Title : Data",
        "image":"https://vipspar.com/wp-content/uploads/2020/08/35013.jpg"
    }
}
from datetime import datetime,time
response=rq.post(fcm_server,headers=headers,data=json.dumps(body))
now=datetime.now().hour
with open(f'response_{d}.json','w+') as f:
    f.write(response.json())
print(post.json())