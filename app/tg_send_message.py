from .Config import API_hash, API_id, Phone_number
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest, DeleteContactsRequest, GetContactIDsRequest
from telethon.tl.types import InputPhoneContact
import asyncio


class Tg_sender:
    def __init__(self, **kwargs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.api_id = API_id
        self.api_hash = API_hash
        self.client = TelegramClient('sender_messagi', api_id=self.api_id, api_hash=self.api_hash, loop= loop).start(Phone_number)
        
#sender_messagi
    def send_to_user(self, user, text):
        with self.client as client:
            entity = client.get_entity(user)
            client.send_message(entity = entity, message = text)
            client(DeleteContactsRequest(id = [entity.id]))
            dialogs = client.get_dialogs()
            client.delete_dialog(dialogs[0])
            
    
    def send_phone(self, phone, text):
            with self.client as client:
                re = client(ImportContactsRequest(
                contacts=[InputPhoneContact(
                client_id = 1,
                phone= phone,
                first_name= phone,
                last_name= phone
                )]
                ))
                entity = client.get_entity(phone)
                client.send_message(entity = entity, message = text)
                client(DeleteContactsRequest(id = [entity.phone]))
                dialogs = client.get_dialogs()
                client.delete_dialog(dialogs[0])
            
