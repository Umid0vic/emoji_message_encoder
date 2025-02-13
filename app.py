from flask import Flask, request, render_template, send_from_directory
from dotenv import load_dotenv
import os
import random

load_dotenv()  # Load environment variables

app = Flask(__name__)

ADSENSE_CLIENT_ID = os.getenv('ADSENSE_CLIENT_ID')
ADSENSE_SLOT_TOP = os.getenv('ADSENSE_SLOT_TOP')
ADSENSE_SLOT_BOTTOM = os.getenv('ADSENSE_SLOT_BOTTOM')

EMOJIS = ["😀", "😃", "😄", "😁", "😆", "🥰", "🤩", "😎", "👻", "🤖"]
MAX_LENGTH = 5000

def byte_to_variation_selector(byte):
    if 0 <= byte <= 15:
        return chr(0xFE00 + byte)
    elif 16 <= byte <= 255:
        return chr(0xE0100 + (byte - 16))
    return None

def variation_selector_to_byte(variation_selector):
    if 0xFE00 <= variation_selector <= 0xFE0F:
        return variation_selector - 0xFE00
    elif 0xE0100 <= variation_selector <= 0xE01EF:
        return (variation_selector - 0xE0100) + 16
    return None

def encode_message(message):
    try:
        byte_values = message.encode('utf-8')
    except UnicodeEncodeError:
        return ""
    encoded_selectors = []
    for byte in byte_values:
        vs = byte_to_variation_selector(byte)
        if vs:
            encoded_selectors.append(vs)
    return ''.join(random.choice(EMOJIS) + vs for vs in encoded_selectors)

def decode_message(encoded_text):
    variation_selectors = []
    for char in encoded_text:
        code_point = ord(char)
        if 0xFE00 <= code_point <= 0xFE0F or 0xE0100 <= code_point <= 0xE01EF:
            variation_selectors.append(code_point)
    decoded_bytes = []
    for vs in variation_selectors:
        byte = variation_selector_to_byte(vs)
        if byte is not None:
            decoded_bytes.append(byte)
    try:
        return bytes(decoded_bytes).decode('utf-8')
    except UnicodeDecodeError:
        return "Decoding error"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_input = request.form.get("text", "")
        if len(user_input) > MAX_LENGTH:
            return render_template("index.html", result="Error: Input exceeds maximum length of 5000 characters")
        
        action = request.form.get("action")
        if action == "encode":
            result = encode_message(user_input)
        elif action == "decode":
            result = decode_message(user_input)
    return render_template("index.html", 
                         result=result,
                         adsense_client_id=ADSENSE_CLIENT_ID,
                         adsense_slot_top=ADSENSE_SLOT_TOP,
                         adsense_slot_bottom=ADSENSE_SLOT_BOTTOM)

@app.route('/ads.txt')
def ads_txt():
    return send_from_directory('static', 'ads.txt')

if __name__ == "__main__":
    app.run(debug=True)