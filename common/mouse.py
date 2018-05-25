# encoding: utf-8
import asyncio


class Mouse(object):

    def __init__(self, page):
        self.page = page

    @staticmethod
    async def __click(page, x, y, click_count=1, button='left', delay=0):
        """
        x <number>
        y <number>
        button <string> left, right, or middle, defaults to left.
        clickCount <number> defaults to 1. See UIEvent.detail.
        delay <number> Time to wait between mousedown and mouseup in milliseconds. Defaults to 0.
        """
        await page.mouse.click(x, y, clickCount=click_count, button=button, delay=delay)

    def click(self, x, y, click_count=1, button='left', delay=0):
        asyncio.get_event_loop().run_until_complete(self.__click(self.page, x, y, click_count=click_count,
                                                            button=button, delay=delay))

    @staticmethod
    async def __down(page, click_count=1, button='left'):
        await page.mouse.down(clickCount=click_count, button=button)

    def down(self, click_count=1, button='left'):
        asyncio.get_event_loop().run_until_complete(self.__down(self.page, click_count=click_count, button=button))

    @staticmethod
    async def __up(page, click_count=1, button='left'):
        await page.mouse.up(clickCount=click_count, button=button)

    def up(self, click_count=1, button='left'):
        asyncio.get_event_loop().run_until_complete(self.__up(self.page, click_count=click_count, button=button))

    @staticmethod
    async def __move(page, x, y, steps=1):
        """
        :param page:
        :param x:
        :param y:
        :param steps:  the steps for this road to complete
        :return:
        """
        await page.mouse.move(x, y, steps=steps)

    def move(self, x, y, steps=1):
        asyncio.get_event_loop().run_until_complete(self.__move(self.page, x=x, y=y, steps=steps))

    @staticmethod
    async def __hover(page, selector):
        await page.mouse.hover(selector)

    def hover(self, selector):
        asyncio.get_event_loop().run_until_complete(self.__hover(self.page, selector=selector))

    def get_x_coordinate(self):
        return self.page.mouse._x

    def get_y_coordinate(self):
        return self.page.mouse._y

