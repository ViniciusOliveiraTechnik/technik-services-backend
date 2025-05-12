import pyotp
import base64
import os

from accounts.utils import CryptoHelper

class OTPHelper:

    def __init__(self):
        
        self.crypto = CryptoHelper()

    def generate_otp_secret(self, length: int = 32) -> bytes:

        random_bytes = os.urandom(length)

        secret = base64.b32encode(random_bytes).decode('utf-8').replace('=', '')

        return self.crypto.encypt(secret)

    def get_totp_uri(self, secret: bytes, email: str, issuer: str = 'Technik') -> str:
        
        secret = self.crypto.decrypt(secret)

        return pyotp.totp.TOTP(secret).provisioning_uri(email, issuer)

    def verify_otp(self, otp_code: str, secret: bytes):
        
        secret = self.crypto.decrypt(secret)

        return pyotp.TOTP(secret).verify(otp_code)