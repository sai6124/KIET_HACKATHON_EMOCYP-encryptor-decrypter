from flask import Flask, render_template, request

from enc_dec import encrypt_to_emojis, decrypt_to_text, emoji_mapping, reverse_emoji_mapping

app = Flask(__name__)

# Load the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Encrypt route
@app.route('/encrypt', methods=['POST'])
def encrypt():
    plain_text = request.form['plain_text']
    emojis_text = encrypt_to_emojis(plain_text)
    return emojis_text

# Decrypt route
@app.route('/decrypt', methods=['POST'])
def decrypt():
    emojis_text = request.form['emojis_text']
    decrypted_text = decrypt_to_text(emojis_text)
    return decrypted_text

if __name__ == "__main__":
    app.run(debug=True)
