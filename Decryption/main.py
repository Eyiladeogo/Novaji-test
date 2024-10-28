from cryptography.hazmat.primitives import padding
import base64

padder = padding.PKCS7(128).padder()
plain_text = padder.update(b"Welcome to Lagos")
plain_text += padder.finalize()
plain_text_as_hex = base64.b16encode(plain_text)
print(plain_text, plain_text_as_hex)

unpadder = padding.PKCS7(128).unpadder()
cipher_text = unpadder.update(plain_text)
cipher_text += unpadder.finalize()
cipher_as_b64 = base64.b16decode(plain_text_as_hex)
print(cipher_text, cipher_as_b64)