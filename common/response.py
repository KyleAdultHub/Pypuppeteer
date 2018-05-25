# encoding: utf-8
import asyncio
from common.request import Request


class Response(object):

    def __init__(self, response):
        self.response = response

    def get_response_headers(self):
        return self.response.headers()

    @staticmethod
    async def __get_response_json(response):
        return await response.json()

    def get_response_json(self):
        return asyncio.get_event_loop().run_until_complete(self.__get_response_json(self.response))

    def response_ok(self):
        return self.response.ok()

    def get_request(self):
        return Request(self.response.request)

    def get_response_status(self):
        return self.response.status()

    @staticmethod
    async def __get_response_content(response):
        return await response.text()

    def get_response_content(self):
        return asyncio.get_event_loop().run_until_complete(self.__get_response_content(self.response))

    def get_response_url(self):
        return self.response.url()
