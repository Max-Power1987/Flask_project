from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired



class My_form(FlaskForm):
    name_user = StringField()
    phone = StringField()
    text_data = TextAreaField()
    my_btn = SubmitField('Отправить сообщение')