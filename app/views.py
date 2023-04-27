from app import app
from flask import render_template
from .tg_send_message import Tg_sender
from .forms import My_form
import asyncio



@app.route('/', methods=['POST', 'GET'])
def index():
    form = My_form()
    if form.is_submitted():
        user = form.name_user.data
        phone = form.phone.data
        text = form.text_data.data
        if len(user) == 0:
            send_to_phone(phone, text)
        else:
            send_to_name_user(user, text)
        form.name_user.data = None
        form.phone.data = None
        form.text_data.data = None
        return render_template('index.html', form = form)
    return render_template('index.html', form = form)

def send_to_phone(phone, text):
    try:
        send = Tg_sender()
        asyncio.run(send.send_phone(phone, text))
    except:
        pass
        
def send_to_name_user(user, text):
    try:
        send = Tg_sender()
        asyncio.run(send.send_to_user(user, text))
    except:
        pass
    
    