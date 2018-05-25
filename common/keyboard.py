# encoding: utf-8
import asyncio


class KeyBoard(object):
    def __init__(self, page):
        self.page = page

    @staticmethod
    async def __type(page, text, delay=0):
        """
        A text to type into a focused element
        """
        await page.keyboard.type(text, delay=delay)

    def type(self, text, delay=0):
        asyncio.get_event_loop().run_until_complete(self.__type(self.page, text, delay=delay))

    @staticmethod
    async def __down(page, key_name):
        await page.keyboard.down(key_name)

    def down(self, key_name):
        asyncio.get_event_loop().run_until_complete(self.__down(self.page, key_name))

    @staticmethod
    async def __up(page, key_name):
        await page.keyboard.up(key_name)

    def up(self, key_name):
        asyncio.get_event_loop().run_until_complete(self.__up(self.page, key_name=key_name))

    @staticmethod
    async def __press(page, key_name, delay=0):
        """
        such as key down and key up
        delay: the time between the key down and key up
        """
        await page.keyboard.press(key_name, delay=delay)

    def press(self, key_name, delay=0):
        asyncio.get_event_loop().run_until_complete(self.__press(self.page, key_name=key_name, delay=delay))

    @staticmethod
    async def __sendCharacter(page, char):
        await page.keyboard.sendCharacter(char)

    def send_character(self, char):
        asyncio.get_event_loop().run_until_complete(self.__sendCharacter(self.page, char))