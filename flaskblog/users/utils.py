import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

This link will expire in 30 minutes for security reasons

If you did not make this request simply ingore this email and no changes will be made.
'''
    mail.send(msg)

def send_confirm_email(user, token, confirm_url):
    msg = Message('Confirm Account', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To confirm your account, visit the following link:
{url_for('users.confirm_email', token=token, _external=True)}

This link will expire in 1 hour for security reasons

'''
    mail.send(msg)
