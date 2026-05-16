import unittest
import requests

BASE_URL = "http://localhost:8000"


class BackendTests(unittest.TestCase):
    # Unique email and username to avoid conflict with existing registrations in mock DB
    test_email = "tester_unit@example.com"
    test_username = "tester_unit"
    test_password = "password123"

    def test_a_register(self):
        # Register a fresh user
        response = requests.post(f"{BASE_URL}/auth/register", json={
            "username": self.test_username,
            "email": self.test_email,
            "password": self.test_password
        })
        # If user already registered in previous runs, accept 400 or 201
        self.assertIn(response.status_code, [201, 400])
        if response.status_code == 201:
            data = response.json()
            self.assertEqual(data["username"], self.test_username)
            self.assertEqual(data["email"], self.test_email)

    def test_b_login(self):
        # Authenticate user
        response = requests.post(f"{BASE_URL}/auth/login", json={
            "email": self.test_email,
            "password": self.test_password
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("access_token", data)
        self.assertEqual(data["token_type"], "bearer")

    def test_c_fetch_user_profile(self):
        # Login to extract access token
        login_response = requests.post(f"{BASE_URL}/auth/login", json={
            "email": self.test_email,
            "password": self.test_password
        })
        token = login_response.json().get("access_token")

        # Fetch profile using authorization bearer header
        response = requests.get(f"{BASE_URL}/users/profile", headers={
            "Authorization": f"Bearer {token}"
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("full_name", data)
        self.assertIn("user_id", data)


if __name__ == "__main__":
    unittest.main()
