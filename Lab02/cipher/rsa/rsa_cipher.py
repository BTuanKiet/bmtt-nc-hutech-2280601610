import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui_file.ui", self)  # Đảm bảo tệp UI đúng

        self.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.btn_sign.clicked.connect(self.call_api_sign)
        self.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        try:
            response = requests.get("http://127.0.0.1:5000/generate_keys")
            data = response.json()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(data["message"])
            msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_encrypt(self):
        try:
            plaintext = self.txt_plain_text.text()
            response = requests.post("http://127.0.0.1:5000/encrypt", json={"plaintext": plaintext})
            data = response.json()
            self.txt_cipher_text.setText(data["encrypted_message"])
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Encrypted Successfully")
            msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_decrypt(self):
        try:
            ciphertext = self.txt_cipher_text.text()
            response = requests.post("http://127.0.0.1:5000/decrypt", json={"ciphertext": ciphertext})
            data = response.json()
            self.txt_plain_text.setText(data["decrypted_message"])
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Decrypted Successfully")
            msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_sign(self):
        try:
            message = self.txt_plain_text.text()
            response = requests.post("http://127.0.0.1:5000/sign", json={"message": message})
            data = response.json()
            self.txt_sign.setText(data["signature"])
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Signed Successfully")
            msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_verify(self):
        try:
            message = self.txt_plain_text.text()
            signature = self.txt_sign.text()
            response = requests.post("http://127.0.0.1:5000/verify", json={"message": message, "signature": signature})
            data = response.json()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Verified Successfully" if data["is_verified"] else "Verified Fail")
            msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptoApp()
    window.show()
    sys.exit(app.exec())
