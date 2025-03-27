import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_QMainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_QMainWindow()
        self.ui.setupUi(self)

        # Verify UI elements
        try:
            self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
            self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        except AttributeError as e:
            QMessageBox.critical(self, "UI Error", f"Missing UI element: {e}")
            sys.exit(1)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()  # Fixed to use text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data.get("encrypted_text", ""))
                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                print(f"Error while calling API: {response.status_code}, {response.text}")
                QMessageBox.critical(self, "Error", f"API Error: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            QMessageBox.critical(self, "Error", f"Request Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()  # Fixed to use text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data.get("decrypted_text", ""))
                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                print(f"Error while calling API: {response.status_code}, {response.text}")
                QMessageBox.critical(self, "Error", f"API Error: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            QMessageBox.critical(self, "Error", f"Request Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
