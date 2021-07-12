import requests
import random
from django.contrib.auth.models import User

def convertTuple(tup):
    str = ''.join(tup)
    return str

def randomemail():
    a= User.objects.values_list('email')
    b= random.choice(a)
    return convertTuple(b)

def send_simple_message(subject, message):
    key = '1fdc8beb76eb73a00c86872d011f6f3b-c4d287b4-b8593eb9'
    sandbox = 'wldhunger.tk'
    recipient = randomemail()

    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'admin@wldhunger.tk',
        'to': recipient,
        'subject': subject,
        'text': message
    })

    print ('Status: {0}'.format(request.status_code))
    print ('Body:   {0}'.format(request.text))
    print (recipient)