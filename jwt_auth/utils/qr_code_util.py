import qrcode
import base64
from io import BytesIO

class QrCodeUtil:

    def __init__(self, value: str):
        
        self.value = value

    def generate(self):

        qr_code = qrcode.make(self.value)

        buffer = BytesIO()

        qr_code.save(buffer, format='PNG')

        buffer.seek(0)

        img_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        return f'data:image/png;base64,{img_base64}'