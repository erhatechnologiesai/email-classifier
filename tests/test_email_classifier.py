import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestEmailClassifier(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_security_classification(self):
        res = self.client.post("/classify-email", json={"subject": "Security Alert: New login from unrecognized device", "body": "Did you just sign in?"})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["category"], "SECURITY")
        self.assertEqual(data["target_folder"], "Security_Alerts")

if __name__ == "__main__":
    unittest.main()
