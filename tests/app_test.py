import unittest
from datetime import date, timedelta
from app import APP


class AppTest(unittest.TestCase):
    HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}

    def test_post_200(self):
        arrival_date = (date.today() + timedelta(days=10)).strftime("%d-%m-%Y")
        tests_data = [{"from_city_code": "AAL", "to_city_code": "GYD", "arrival_date": arrival_date},
                      {"from_city_code": "BUS", "to_city_code": "ZVJ", "arrival_date": arrival_date}]
        tester = APP.test_client(self)
        for test_data in tests_data:
            response = tester.post("/home_page", data=test_data, headers=self.HEADERS)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/html")
            self.assertTrue(b"DOCTYPE" in response.data)

    def test_post_400(self):
        arrival_date = (date.today() - timedelta(days=10)).strftime("%d-%m-%Y")
        tests_data = [{"from_city_code": "AAL", "to_city_code": "GYD", "arrival_date": arrival_date},
                      {"from_city_code": "BUS", "to_city_code": "ZVJ", "arrival_date": arrival_date}]
        tester = APP.test_client(self)
        for test_data in tests_data:
            response = tester.post("/home_page", data=test_data, headers=self.HEADERS)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.content_type, "text/html")
            self.assertTrue(b"DOCTYPE" in response.data)


if __name__ == '__main__':
    unittest.main()
