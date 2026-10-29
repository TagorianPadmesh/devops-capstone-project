"""Tests for the Customer Accounts REST API."""
import unittest
from service import create_app
from service.models import store


class AccountApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app({"TESTING": True, "TALISMAN_FORCE_HTTPS": False})
        self.client = self.app.test_client()
        store.clear()

    def payload(self):
        return {"name": "Ada Lovelace", "email": "ada@example.com", "address": "London"}

    def test_create_account(self):
        response = self.client.post("/accounts", json=self.payload())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["name"], "Ada Lovelace")

    def test_list_accounts(self):
        self.client.post("/accounts", json=self.payload())
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_read_account(self):
        created = self.client.post("/accounts", json=self.payload()).get_json()
        response = self.client.get(f"/accounts/{created['id']}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["email"], "ada@example.com")

    def test_read_missing_account(self):
        self.assertEqual(self.client.get("/accounts/99").status_code, 404)

    def test_update_account(self):
        created = self.client.post("/accounts", json=self.payload()).get_json()
        response = self.client.put(f"/accounts/{created['id']}", json={"name": "Ada Byron"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Ada Byron")

    def test_delete_account(self):
        created = self.client.post("/accounts", json=self.payload()).get_json()
        response = self.client.delete(f"/accounts/{created['id']}")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.client.get(f"/accounts/{created['id']}").status_code, 404)

    def test_create_requires_fields(self):
        response = self.client.post("/accounts", json={"name": "Incomplete"})
        self.assertEqual(response.status_code, 400)

    def test_security_headers_and_cors(self):
        response = self.client.get("/accounts", headers={"Origin": "https://example.com"})
        self.assertIn("X-Content-Type-Options", response.headers)
        self.assertIn("Access-Control-Allow-Origin", response.headers)


if __name__ == "__main__":
    unittest.main()
