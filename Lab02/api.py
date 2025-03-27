from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher
app = Flask(__name__)

caesar_cipher = CaesarCipher()
vigenere_Cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()
ecc_cipher = ECCCipher()
# rsa_cipher = RSACipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_Cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_Cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'matrix': playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.transposition_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.transposition_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# @app.route('/api/rsa/generate_keys', methods=['GET'])
# def rsa_generate_keys():
#     rsa_cipher.generate_keys()
#     return jsonify({'message': 'Keys generated successfully'})

# @app.route('/api/rsa/encrypt', methods=['POST'])
# def rsa_encrypt():
#     data = request.json
#     message = data['message']
#     key_type = data['key_type']
#     private_key, public_key = rsa_cipher.load_keys()
    
#     if key_type == 'public':
#         key = public_key
#     elif key_type == 'private':
#         key = private_key
#     else:
#         return jsonify({'error': 'Invalid key type'})
    
#     encrypted_message = rsa_cipher.encrypt(message, key)
#     encrypted_hex = encrypted_message.hex()
#     return jsonify({'encrypted_message': encrypted_hex})

# @app.route('/api/rsa/decrypt', methods=['POST'])
# def rsa_decrypt():
#     data = request.json
#     ciphertext_hex = data['ciphertext']
#     key_type = data['key_type']
#     private_key, public_key = rsa_cipher.load_keys()
    
#     if key_type == 'public':
#         key = public_key
#     elif key_type == 'private':
#         key = private_key
#     else:
#         return jsonify({'error': 'Invalid key type'})
    
#     ciphertext = bytes.fromhex(ciphertext_hex)
#     decrypted_message = rsa_cipher.decrypt(ciphertext, key)
#     return jsonify({'decrypted_message': decrypted_message})

# @app.route('/api/rsa/sign', methods=['POST'])
# def rsa_sign_message():
#     data = request.json
#     message = data['message']
#     private_key, _ = rsa_cipher.load_keys()
    
#     signature = rsa_cipher.sign(message, private_key)
#     signature_hex = signature.hex()
#     return jsonify({'signature': signature_hex})

# @app.route('/api/rsa/verify', methods=['POST'])
# def rsa_verify_signature():
#     data = request.json
#     message = data['message']
#     signature_hex = data['signature']
#     public_key, _ = rsa_cipher.load_keys()
    
#     signature = bytes.fromhex(signature_hex)
#     is_verified = rsa_cipher.verify(message, signature, public_key)
#     return jsonify({'is_verified': is_verified})

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)