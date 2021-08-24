import unittest
import json
from api import app
from methods import Token, Restricted


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token(self):
        with app.app_context():
            self.assertEqual(
                "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiYWRtaW4ifQ.m8UshTqghHSrbjd9O_xaHdQx-G4m4sz6JWCffMhvFtDTpCdqd30QKe-iFp0BjosWcL0htQnHhhi3qv_ec4zhew",
                self.convert.generate_token("admin", "secret"),
            )

    def test_access_data(self):
        self.assertEqual(
            "You are under protected data",
            self.validate.access_data(
                "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiYWRtaW4ifQ.m8UshTqghHSrbjd9O_xaHdQx-G4m4sz6JWCffMhvFtDTpCdqd30QKe-iFp0BjosWcL0htQnHhhi3qv_ec4zhew"
            ),
        )


class TestRequestMethods(unittest.TestCase):
    def setUp(self):
        self.convert = Token()
        self.client = app.test_client()

    def test_login(
        self,
    ):
        mimetype = "application/json"
        headers = {"Content-Type": mimetype, "Accept": mimetype}
        response = self.client.post(
            "/login",
            data={"username": "admin", "password": "secret"},
            headers=headers,
            content_type="application/x-www-form-urlencoded",
        )

        data = json.loads(response.data)

        self.assertEqual(
            data["data"],
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiYWRtaW4ifQ.m8UshTqghHSrbjd9O_xaHdQx-G4m4sz6JWCffMhvFtDTpCdqd30QKe-iFp0BjosWcL0htQnHhhi3qv_ec4zhew",
        )

    def test_protected(self):
        with app.app_context():
            token = self.convert.generate_token("admin", "secret")
            mimetype = "application/json"
            headers = {
                "Content-Type": mimetype,
                "Accept": mimetype,
                "Authorization": token,
            }
            response = self.client.get("/protected", headers=headers)

            data = json.loads(response.data)

            self.assertEqual(data["data"], "You are under protected data")


if __name__ == "__main__":
    unittest.main()
