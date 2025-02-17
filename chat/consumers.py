# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

ALLOWED_ROOMS = ['1', '2', '3']

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        # Close if the page does not belong to the created pages
        if self.room_name not in ALLOWED_ROOMS:
            await self.close() 
            return

        self.room_group_name = f'chat_{self.room_name}'

        # Add a new group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Exit the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        nickname = text_data_json['nickname']

        # Send a message with the nickname
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'nickname': nickname,
                
            }
        )

    async def chat_message(self, event):
        message = event['message']
        nickname = event['nickname']

        # Send the messagge to the websocket
        await self.send(text_data=json.dumps({
            'message': message,
            'nickname': nickname
        }))