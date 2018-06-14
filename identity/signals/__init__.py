from .signals import *
from .handlers import *

send_email_signal.connect(send_email_handler,
                          dispatch_uid='send_email')

