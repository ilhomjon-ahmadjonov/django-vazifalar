import re
from rest_framework.exceptions import ValidationError
phone_regex = re.compile(r'^998(9[012345789]|6[125679]|7[01234569])[0-9]{7}$')
email_regex = re.compile( r'^[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.[A-Za-z0-9-_.+/=]+$')

def email_or_phone_regex(user_input):
    if re.fullmatch(phone_regex, user_input):
        return 'phone'

    elif re.fullmatch(email_regex,user_input):
        return 'email'

    
    raise ValidationError('Email yoki telefon raqam xato kiritdingiz')