import re
from django.core.exceptions import ValidationError

def validate_cnpj(value):
    regex = r'([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})'

    if not re.match(regex, value):
        raise ValidationError('CNPJ inválido.')
