import pyotp
import os
import base64

from accounts.utils import CryptoUtil

class OTPUtil:

    def __init__(self):
        
        self.crypto_util = CryptoUtil()

    def generate_otp_secret(self, length: int = 32) -> bytes:

        random_bytes = os.urandom(length)

        secret = base64.b32encode(random_bytes).decode('utf-8').replace('=', '')

        return self.crypto_util.encypt(secret)

    def get_totp_uri(self, user_secret: bytes, email: str, issuer: str = 'Technik') -> str:
        
        user_secret = self.crypto_util.decrypt(user_secret)

        return pyotp.totp.TOTP(user_secret).provisioning_uri(email, issuer)
    
    def verify_otp(self, otp_code: str, user_secret: bytes):

        user_secret = self.crypto_util.decrypt(user_secret)

        return pyotp.TOTP(user_secret).verify(otp_code)
