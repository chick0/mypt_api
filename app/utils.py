from functools import wraps
from time import time as timestamp

from flask import request
from flask import jsonify
from jwt import decode
from jwt.exceptions import InvalidSignatureError

from app.token import algorithms
from app.secret_key import SECRET_KEY


def error(code: int, message: str):
    return jsonify({
        "code": code,
        "message": message
    }), code


def parse_tags(tag_str: str) -> list:
    return [x for x in [this.strip() for this in tag_str.split(",")] if len(x) != 0]


def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get("x-auth", "meowed")

        try:
            token = decode(
                jwt=token,
                key=SECRET_KEY.hex(),
                algorithms=algorithms
            )
        except (InvalidSignatureError, Exception):
            return error(
                code=400,
                message="인증 토큰 검증에 실패했습니다."
            )

        try:
            if token['time']['a'] < round(timestamp()) <= token['time']['b']:
                # 만료되지 않은 토큰
                pass
            else:
                return error(
                    code=401,
                    message="만료된 인증토큰 입니다."
                )

            if token['host'] != request.host:
                return error(
                    code=403,
                    message="토큰을 생성한 API 서버가 다릅니다."
                )

            if token['client'] != request.origin:
                return error(
                    code=403,
                    message="토큰을 생성한 클라이언트가 다릅니다."
                )
        except KeyError:
            return error(
                code=400,
                message="토큰 형식이 올바르지 않습니다."
            )

        return f(*args, **kwargs, payload=token)

    return decorator