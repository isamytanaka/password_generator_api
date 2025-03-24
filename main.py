from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

def generate_password(length=12, numbers=True, specials=True):
    characters = string.ascii_letters
    if numbers:
        characters += string.digits
    if specials:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/generate_password', methods=['GET'])
def api_generate_password():
    length = request.args.get('length', default=12, type=int)
    numbers = request.args.get('numbers', default=True, type=lambda v: v.lower() == 'true')
    specials = request.args.get('specials', default=True, type=lambda v: v.lower() == 'true')

    password = generate_password(length, numbers, specials)
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)