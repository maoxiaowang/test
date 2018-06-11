from django.dispatch import Signal


send_email_signal = Signal(
    providing_args=['subject', 'from_email', 'to', 'content', 'content_type']
)
