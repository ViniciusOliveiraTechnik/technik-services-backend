from cryptography.fernet import Fernet

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

class CryptoUtil:

    def __init__(self):
        
        self.key = settings.ENCRYPTION_KEY

    def get_fernet(self):

        if not self.key:

            raise ImproperlyConfigured("ENCRYPTION_KEY not set in environment variables")
        
        return Fernet(self.key)
    
    def encypt(self, data: str) -> bytes:

        fernet = self.get_fernet()

        return fernet.encrypt(data.encode())
    
    def decrypt(self, data: bytes):

        fernet = self.get_fernet()

        if isinstance(data, memoryview):

            data = data.tobytes()

        if not data or not isinstance(data, (bytes, bytearray)):

            raise ValueError('The data value type is not a byte type')
        
        return fernet.decrypt(data).decode()