from datetime import datetime
import requests
from bs4 import BeautifulSoup
from spider.init_spider import _get_headers


class Spider:
    def __init__(self):
        self.headers = _get_headers()
        self.url = "https://fly2.emirates.com/CAB/SessionHandler.aspx?target=%2fIBE.aspx&pub=%2fenglish&h" \
                   "=cc6c2c618373d871bffa5aaf308f53bded13aa70&FlexOnly="

    def parse(self, params) -> dict:
        response = self._get_response(params)
        result = self._extract_data(response)
        return result

    @staticmethod
    def _extract_data(response) -> dict:
        soap = BeautifulSoup(response.text, 'html.parser')
        results = {"results": [], "deep_link": response.url}
        tickets_block = soap.find("div", {"id": "interline-flight-list"})
        if tickets_block:
            tickets = tickets_block.find_all("div", class_="flights-row")[0:3]
            for ticket in tickets:
                flight_price = ticket.find("div", class_="ts-ifl-row__footer-price").text
                flight_time = ticket.find("div", class_="ts-fie__infographic").find("time").find_all("span")[-1].text
                results["results"].append({"flight_time": flight_time.strip(), "flight_price": flight_price.strip()})
        return results

    def _get_response(self, params) -> requests:
        payload = self._built_payload(params)
        response = requests.request("POST", url=self.url, headers=self.headers, data=payload)
        return response

    @staticmethod
    def _built_payload(params) -> str:
        from_city_code, to_city_code = params["from_city_code"], params["to_city_code"]
        date = datetime.strptime(params["arrival_date"], "%d-%m-%Y").strftime("%d-%b-%-y")
        payload = f'j=t&seldcity1={from_city_code}&selacity1={to_city_code}&selddate1={date}&seladults=1&TID=OW'
        return payload
