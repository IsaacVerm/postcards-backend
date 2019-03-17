from flask import jsonify


def credentials(name):
    if name == "me":
        return jsonify(user='myself', password='sense')
    if name == "you":
        return jsonify(user='yourself', password='nonsense')
    else:
        return ''
