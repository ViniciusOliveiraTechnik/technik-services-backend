import re
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException

class PhoneUtil:

    def __init__(self, phone_number_region: str = 'BR'):

        if not phone_number_region or not isinstance(phone_number_region, str):

            raise ValueError('A região de contato deve ser um valor de texto válido')
        
        self.phone_number_region = phone_number_region

    def normalize(self, phone_number: str) -> str:

        if not phone_number or not isinstance(phone_number, str):

            raise ValueError('O número de contato deve ser um valor de texto válido')

        digits_only = re.sub(r'\D', '', phone_number)

        try:

            parsed_phone = phonenumbers.parse(digits_only, self.phone_number_region)

            if not phonenumbers.is_valid_number(parsed_phone):

                return digits_only

            return phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
        
        except NumberParseException:

            return digits_only

    def validate(self, phone: str) -> bool:

        if not phone or not isinstance(phone, str):

            raise ValueError('Número de telefone deve ser passado como string')

        digits_only = re.sub(r'\D', '', phone)

        try:

            parsed_phone = phonenumbers.parse(digits_only, self.phone_number_region)

            return phonenumbers.is_valid_number(parsed_phone)
        
        except NumberParseException:

            return False

    def mask(self, phone: str) -> str:

        if not phone or not isinstance(phone, str):

            raise ValueError('Número de telefone deve ser passado como string')

        try:

            parsed_phone = phonenumbers.parse(phone, self.phone_number_region)

            if not phonenumbers.is_valid_number(parsed_phone):

                return phone

            return phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        
        except NumberParseException:
            
            return phone
