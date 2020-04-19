import unittest, flask_testing, requests, os
import app

class ServerIntegrationTestCase(
    flask_testing.LiveServerTestCase
):
    def create_app(self):
        return app.app

    def test_server_status_code(self):
        response = requests.get(self.get_server_url())
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()