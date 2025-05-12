import re
import hashlib
from validate_docbr import CPF

from django.conf import settings

from accounts.utils import CryptoHelper

class CPFHelper:

    def __init__(self):
        
        self.cpf_validator = CPF()
        self.crypto_helper = CryptoHelper()

    def normalize(self, cpf: str) -> str:
        
        if not cpf or not isinstance(cpf, str):

            raise ValueError('CPF is not passed by argument or type is not string')
        
        return re.sub(r'\D', '', cpf)
    
    def validate(self, cpf: str) -> bool:

        if not cpf or not isinstance(cpf, str):

            raise ValueError('CPF is not passed by argument or type is not string')
        
        normalized_cpf = self.normalize(cpf)

        return self.cpf_validator.validate(normalized_cpf)
    
    def mask(self, cpf: str) -> str:

        if not cpf or not isinstance(cpf, str):

            raise ValueError('CPF is not passed by argument or type is not string')
        
        normalized_cpf = self.normalize(cpf)

        return self.cpf_validator.mask(normalized_cpf)
    
    def create_hash(self, cpf: str, salt: str = settings.CPF_HASH_SALT) -> str:

        if not cpf or not salt:

            raise ValueError('CPF or Salt is invalid')

        normalized_cpf = self.normalize(cpf)

        return hashlib.sha256((salt + normalized_cpf).encode()).hexdigest()

    def encrypt(self, cpf: str) -> bytes:

        if not cpf or not isinstance(cpf, str):

            raise ValueError('CPF is not passed by argument or type is not string')

        normalized_cpf = self.normalize(cpf)

        return self.crypto_helper.encypt(normalized_cpf)
    
    def decrypt(self, encrypted_cpf: bytes):

        return self.crypto_helper.decrypt(encrypted_cpf)
