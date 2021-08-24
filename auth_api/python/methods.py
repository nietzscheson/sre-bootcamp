import os
import logging
import hashlib
from models import User
import jwt
from jwt.exceptions import DecodeError, ExpiredSignatureError, InvalidSignatureError

env = os.environ
logger = logging.getLogger(__name__)


class Token:
    def generate_token(self, username, password):
        try:

            user = User.query.filter_by(username=username).first()

            if user is None:
                raise Exception(f"The {username} User don't exists")

            hashed = hashlib.sha512(
                str(password + user.salt).encode("utf-8")
            ).hexdigest()

            if hashed != user.password:
                raise Exception("Invalid credentials")

            encoded_jwt = jwt.encode(
                {"role": user.role}, env["JWT_SECRET"], algorithm="HS512"
            )
            return encoded_jwt
        except Exception as errors:
            logger.exception(errors)


def token_verify(authorization):
    try:
        token = str.replace(str(authorization), "Bearer ", "")

        jwt.decode(token, env["JWT_SECRET"], algorithms=["HS512"])
        return True
    except DecodeError:
        return False
    except ExpiredSignatureError:
        return False
    except InvalidSignatureError:
        return False


class Restricted:
    def access_data(self, authorization):

        if token_verify(authorization):
            return "You are under protected data"

        return "Access Denied, Invalid Token"
