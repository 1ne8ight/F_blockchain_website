#class de configuration de nos parametres mail

class Config :
    MAIL_SERVER = 'smtp.gmail.com' 
    MAIL_PORT =  465
    MAIL_USE_TLS = False 
    MAIL_USE_SSL =  True
    MAIL_USERNAME =  'tanoheliezerbonny@gmail.com'
    MAIL_PASSWORD = 'djmblwifkrknklog'

    MAIL_DEBUG = True   
    MAIL_SUPPRESS_SEND = False

    MAIL_DEFAULT_SENDER = ('Flask Mailer', 'tanoheliezer@gmail.com')
    MAIL_MAX_EMAILS = None
    MAIL_ASCII_ATTACHMENTS = False