from datetime import datetime
from flask import Flask, request, render_template, make_response
from flask_api import status
from flask_restful import Api, Resource
from spider.spider import Spider

APP = Flask(__name__)
API = Api(APP)


class MainPage(Resource):
    DEFAULT_HEADERS = {'Content-Type': 'text/html'}

    def get(self):
        rendered_result = render_template("home_page/home_page.html")
        return make_response(rendered_result, status.HTTP_200_OK, self.DEFAULT_HEADERS)

    def post(self):
        params = dict(request.form)
        if self._is_correct_arrival_date(params):
            results = Spider().parse(params)
            status_code = status.HTTP_200_OK
        else:
            results = {"result": "Bad arrival date. Date cannot be in the past!"}
            status_code = status.HTTP_400_BAD_REQUEST
        rendered_result = render_template("home_page/home_page.html", results=results)
        return make_response(rendered_result, status_code, self.DEFAULT_HEADERS)

    @staticmethod
    def _is_correct_arrival_date(params) -> bool:
        arrival_date = datetime.strptime(params["arrival_date"], "%d-%m-%Y")
        is_correct = arrival_date >= datetime.now()
        return is_correct


API.add_resource(MainPage, "/home_page")


if __name__ == "__main__":
    APP.run(debug=True)
