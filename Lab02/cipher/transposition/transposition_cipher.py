class TranspositionCipher:
    def __init__(self):
        pass

    def transposition_encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            poiner = col
            while poiner < len(text):
                encrypted_text += text[poiner]
                poiner += key
        return encrypted_text
    
    def transposition_decrypt(self, text, key):
        decrypted_text = [''] * key
        col = 0
        row = 0
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1
        return ''.join(decrypted_text)