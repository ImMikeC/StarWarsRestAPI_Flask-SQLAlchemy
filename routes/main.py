from flask import Blueprint, jsonify, request

bpMain = Blueprint('bpMain', __name__)

@bpMain.route('/')
def main():
    return jsonify({
        "message": "This is my Star Wars REST API code"
    }), 200

    