import json
from channels.generic.websocket import WebsocketConsumer
from .models import User


class TweetConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        
        # req_id = data['req_id']
        # req_label = data['req_label']
        # payload = data['payload']
        print(data)
        message = data['payload']['user_email']
        print(message)
        self.send(text_data=json.dumps({
            'message': message + ' from server'
        }))


class UserConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        req_id = data['req_id']
        req_label = data['req_label']
        payload = data['payload']['user_email']

        if req_label == 'CREATE_USER':
            u = User(email=payload).save()
            print(u)
            self.send(text_data=json.dumps({
                'req_id': req_id,
                'req_label': req_label,
                'status': 'SUCCESSFUL',
                'user': u
            }))
