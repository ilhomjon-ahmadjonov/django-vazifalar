import re
from rest_framework.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings

phone_regex = re.compile(r'^998(9[012345789]|6[125679]|7[01234569])[0-9]{7}$')
email_regex = re.compile( r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def email_or_phone_regex(user_input):
    if re.fullmatch(phone_regex, user_input):
        return 'phone'

    elif re.fullmatch(email_regex,user_input):
        return 'email'

    
    raise ValidationError('Email yoki telefon raqam xato kiritdingiz')


def send_code(email, code):
    subject = "Online Shop - Tasdiqlash kodi"
    message = f"Assalomu alaykum!\n\nSizning tasdiqlash kodingiz: {code}\nUshbu kodni hech kimga bermang."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False
    )