import rsa
import os

class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        # Tạo cặp khóa mới với độ dài 512 bits (có thể tăng lên cho bảo mật cao hơn)
        (self.public_key, self.private_key) = rsa.newkeys(512)
        with open("private.pem", "wb") as priv_file:
            priv_file.write(self.private_key.save_pkcs1("PEM"))
        with open("public.pem", "wb") as pub_file:
            pub_file.write(self.public_key.save_pkcs1("PEM"))

    def load_keys(self):
        # Nếu file chưa tồn tại thì tạo mới
        if not os.path.exists("private.pem") or not os.path.exists("public.pem"):
            self.generate_keys()
        with open("private.pem", "rb") as priv_file:
            private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())
        with open("public.pem", "rb") as pub_file:
            public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
        return private_key, public_key

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode(), key)

    def decrypt(self, ciphertext, key):
        return rsa.decrypt(ciphertext, key).decode()

    def sign(self, message, private_key):
        return rsa.sign(message.encode(), private_key, "SHA-256")

    def verify(self, message, signature, public_key):
        try:
            rsa.verify(message.encode(), signature, public_key)
            return True
        except rsa.VerificationError:
            return False
