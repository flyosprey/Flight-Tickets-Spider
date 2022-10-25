import unittest
from datetime import date, timedelta
from spider.spider import Spider


class SpiderTest(unittest.TestCase):
    def test_get_response(self):
        spider_obj = Spider()
        arrival_date = (date.today() + timedelta(days=10)).strftime("%d-%m-%Y")
        tests_data = [{"from_city_code": "AAL", "to_city_code": "GYD", "arrival_date": arrival_date},
                      {"from_city_code": "BUS", "to_city_code": "ZVJ", "arrival_date": arrival_date}]
        for test_data in tests_data:
            response = spider_obj._get_response(test_data)
            self.assertEqual(response.status_code, 200)
            self.assertTrue("DOCTYPE" in response.text)

    def test_extract_data(self):
        spider_obj = Spider()
        arrival_date = (date.today() + timedelta(days=10)).strftime("%d-%m-%Y")
        tests_data = [{"from_city_code": "AAL", "to_city_code": "GYD", "arrival_date": arrival_date},
                      {"from_city_code": "BUS", "to_city_code": "ZVJ", "arrival_date": arrival_date}]
        for test_data in tests_data:
            response = spider_obj._get_response(test_data)
            results = spider_obj._extract_data(response)
            self.assertTrue(isinstance(results, dict))
            self.assertTrue("results" in results)
            self.assertTrue("deep_link" in results)
            self.assertTrue(isinstance(results["results"], list))


if __name__ == '__main__':
    unittest.main()
