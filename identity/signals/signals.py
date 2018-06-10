from django.dispatch import Signal


send_email_signal = Signal(
    providing_args=['subject', 'message', 'identifier']
)
