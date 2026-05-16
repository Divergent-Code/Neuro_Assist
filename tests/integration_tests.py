import unittest
import requests

BASE_URL = "http://localhost:8000"


class IntegrationTests(unittest.TestCase):
    test_username = "tester_integration"
    test_email = "tester_integration@example.com"
    test_password = "TestPassword123!"

    def test_a_homepage(self):
        response = requests.get(f"{BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertIn("Neuro-Assist API", response.json()["message"])

    def test_b_user_registration(self):
        payload = {
            "username": self.test_username,
            "email": self.test_email,
            "password": self.test_password
        }
        response = requests.post(f"{BASE_URL}/auth/register", json=payload)
        self.assertIn(response.status_code, [201, 400])

    def test_c_user_login(self):
        payload = {
            "email": self.test_email,
            "password": self.test_password
        }
        response = requests.post(f"{BASE_URL}/auth/login", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())

    def test_d_get_learning_materials(self):
        response = requests.get(f"{BASE_URL}/learning/materials")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_e_get_job_listings(self):
        response = requests.get(f"{BASE_URL}/jobs")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_f_get_routine_tasks(self):
        response = requests.get(f"{BASE_URL}/routine/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_g_get_health_entries(self):
        response = requests.get(f"{BASE_URL}/health/entries")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)


if __name__ == "__main__":
    unittest.main()
