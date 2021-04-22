import keyring

class Config:
	SECRET_KEY = keyring.get_password("flaskblog", "secret")
	SQLALCHEMY_DATABASE_URI = keyring.get_password("flaskblog", "dburi")
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = keyring.get_password("flaskblog", "guser")
	MAIL_PASSWORD = keyring.get_password("flaskblog", "gpass")
	SECURITY_PASSWORD_SALT = keyring.get_password("flaskblog", "passsalt")