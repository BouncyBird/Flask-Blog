import os

class Config:
	SECRET_KEY = os.getenv("secret")
	SQLALCHEMY_DATABASE_URI = os.getenv("dburi")
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.getenv("guser")
	MAIL_PASSWORD = os.getenv("gpass")
	SECURITY_PASSWORD_SALT = os.getenv("passsalt")
