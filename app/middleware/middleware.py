from functools import wraps
from flask import request, jsonify, current_app


def api_key_required(f):
    @wraps(f)
    def decorated_api_required(*args, **kwargs):
        token = None
        if 'x-api-access-token' in request.headers:
            token = request.headers['x-api-access-token']
        else:
            return jsonify({
                "error": "Un-Authorized access"
            }), 401
        if token != current_app.config['API_KEY']:
            return jsonify({
                "error": "API KEY doesn't match"
            }), 401
        return f(*args, **kwargs)

    return decorated_api_required
