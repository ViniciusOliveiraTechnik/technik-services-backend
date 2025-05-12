import io
import base64
import qrcode

def generate_totp_qrcode(totp_uri: str):

    if not totp_uri:

        raise ValueError("A uri TOTP não é válida")

    qr_code_image = qrcode.make(totp_uri)

    buffered = io.BytesIO()

    qr_code_image.save(buffered, format="PNG")

    string_qr_code_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return f"data:image/png;base64,{string_qr_code_image}"