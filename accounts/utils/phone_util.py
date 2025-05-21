import re
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException

class PhoneUtil:

    def __init__(self, default_region: str = 'BR'):

        if not default_region or not isinstance(default_region, str):

            raise ValueError('Região padrão deve ser uma string válida')
        
        self.default_region = default_region

    def normalize(self, phone: str) -> str:
        """
        Normalize a phone number to E.164 format.

        Args:
            phone (str): Phone number as a string.

        Returns:
            str: Phone number in E.164 format if valid, else digits-only version.
        """
        if not phone or not isinstance(phone, str):

            raise ValueError('Número de telefone deve ser passado como string')

        digits_only = re.sub(r'\D', '', phone)

        try:

            parsed_phone = phonenumbers.parse(digits_only, self.default_region)

            if not phonenumbers.is_valid_number(parsed_phone):

                return digits_only

            return phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
        
        except NumberParseException:

            return digits_only

    def validate(self, phone: str) -> bool:
        """
        Validate if a phone number is valid in the given region.

        Args:
            phone (str): Phone number as a string.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not phone or not isinstance(phone, str):

            raise ValueError('Número de telefone deve ser passado como string')

        digits_only = re.sub(r'\D', '', phone)

        try:

            parsed_phone = phonenumbers.parse(digits_only, self.default_region)

            return phonenumbers.is_valid_number(parsed_phone)
        
        except NumberParseException:

            return False

    def mask(self, phone: str) -> str:
        """
        Mask the phone number using international format.

        Args:
            phone (str): Phone number in E.164 format or raw.

        Returns:
            str: Phone number in INTERNATIONAL format if valid, else input value.
        """
        if not phone or not isinstance(phone, str):

            raise ValueError('Número de telefone deve ser passado como string')

        try:

            parsed_phone = phonenumbers.parse(phone, self.default_region)

            if not phonenumbers.is_valid_number(parsed_phone):

                return phone

            return phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        
        except NumberParseException:
            
            return phone
