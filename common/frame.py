# encoding: utf-8
import asyncio
from common.element import Element


class Frame(object):

    def __init__(self, frame):
        self.frame = frame

    @staticmethod
    async def __get_element_by_selector(frame, selector):
        return await frame.quirySelector(selector)

    def get_element_by_selector(self, selector):
        return Element(asyncio.get_event_loop().run_until_complete(self.__get_element_by_selector(self.frame, selector=selector)))

    @staticmethod
    async def __get_elements_by_selector(frame, selector):
        return await frame.quirySelectorAll(selector)

    def get_elements_by_selector(self, selector):
        return [Element(i) for i in asyncio.get_event_loop().run_until_complete(self.__get_elements_by_selector(self.frame, selector=selector))]

    @staticmethod
    async def __get_elements_by_xpath(frame, xpath):
        return await frame.xpath(xpath)

    def get_elements_by_xpath(self, xpath):
        return [Element(i) for i in asyncio.get_event_loop().run_until_complete(self.__get_elements_by_xpath(self.frame, xpath=xpath))]