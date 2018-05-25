# encoding: utf-8
import asyncio


class Element(object):

    def __init__(self, element):
        self.element = element

    @staticmethod
    async def __querySelector(element, selector):
        """
        :param element: the father element
        :param selector: a selector to query element for  string
        :return: <?ElementHandle>
        """
        return await element.querySelector(selector=selector)

    def get_element_by_selector(self, selector):
        """
        :param element: the father element
        :param selector: a selector to query element for  string
        :return: <?ElementHandle>
        """
        return Element(asyncio.get_event_loop().run_until_complete(self.__querySelector(self.element, selector=selector)))

    @staticmethod
    async def __querySelectorAll(element, selector):
        """
        :param element: the father element
        :param selector: a selector to query element for  string
        :return: <?ElementHandle> n  list
        """
        return await element.quirySelectorAll(selector)

    def get_elements_by_selector(self, selector):
        """
        :param element: the father element
        :param selector: a selector to query element for  string
        :return: <?ElementHandle> n  list
        """
        return [Element(i) for i in asyncio.get_event_loop().run_until_complete(self.__querySelectorAll(self.element, selector=selector))]

    @staticmethod
    async def __get_elements_by_xpath(element, xpath):
        """
        :param element: the father element
        :param xpath:  the string to query element in the page source
        :return: list contain all element for selector
        """
        return await element.xpath(xpath)

    def get_elements_by_xpath(self, xpath):
        """
        :param element: the father element
        :param xpath:  the string to query element in the page source
        :return: list contain all element for selector
        """
        return [Element(i) for i in asyncio.get_event_loop().run_until_complete(self.__get_elements_by_xpath(self.element, xpath=xpath))]

    @staticmethod
    async def __click(element, click_count=1, button='left', delay=0):
        """
        element: the target element
        button <string> left, right, or middle, defaults to left.
        clickCount <number> defaults to 1. See UIEvent.detail.
        delay <number> Time to wait between mousedown and mouseup in milliseconds. Defaults to 0.
        """
        await element.click(clickCount=click_count, button=button, delay=delay)

    def click(self, click_count=1, button='left', delay=0):
        """
        element: the target element
        button <string> left, right, or middle, defaults to left.
        clickCount <number> defaults to 1. See UIEvent.detail.
        delay <number> Time to wait between mousedown and mouseup in milliseconds. Defaults to 0.
        """
        asyncio.get_event_loop().run_until_complete(self.__click(self.element, click_count=click_count, button=button, delay=delay))

    @staticmethod
    async def __get_content_frame(element):
        return await element.contentFrame(element)

    def get_content_frame(self):
        from common.frame import Frame
        return Frame(asyncio.get_event_loop().run_until_complete(self.__get_content_frame(self.element)))

    @staticmethod
    async def __focus(element):
        await element.focus()

    def focus(self):
        asyncio.get_event_loop().run_until_complete(self.__focus(self.element))

    @staticmethod
    async def __hover(element):
        await element.hover()

    def hover(self):
        asyncio.get_event_loop().run_until_complete(self.__hover(self.element))

    @staticmethod
    async def __press(element, key_name, delay=0):
        """
        Focuses the element, and then uses keyboard.down and keyboard.up.
        delay: the time between the key down and key up
        """
        await element.press(key_name, delay=delay)

    def press(self, element, key_name, delay=0):
        """
        Focuses the element, and then uses keyboard.down and keyboard.up.
        delay: the time between the key down and key up
        """
        asyncio.get_event_loop().run_until_complete(self.__press(self.element, key_name, delay=delay))

    def get_element_string(self):
        return self.element.toString()

    @staticmethod
    async def __type(element, text, delay=0):
        """
        Focuses the element, and then sends a keydown, keypress/input, and keyup event for each character in the text.
        """
        await element.type(text, delay=delay)

    def type(self, text, delay=0):
        asyncio.get_event_loop().run_until_complete(self.__type(self.element, text, delay=delay))

    @staticmethod
    async def __uploadFile(element, file_paths):
        await element.uploadFie(file_paths)

    def upload_file(self, file_paths):
        asyncio.get_event_loop().run_until_complete(self.__uploadFile(self.element, file_paths))

    @staticmethod
    async def __get_screenshot(element, type='png', fullPage=False, omitBackground=False, **kwargs):
        """
        path     <string> The file path to save the image to. The screenshot type will be inferred from file extension. If path is a relative path, then it is resolved relative to current working directory. If no path is provided, the image won't be saved to the disk.
        type     <string> Specify screenshot type, can be either jpeg or png. Defaults to 'png'.
        quality  <number> The quality of the image, between 0-100. Not applicable to png images.
        fullPage <boolean> When true, takes a screenshot of the full scrollable page. Defaults to false.
        clip     <dict> An object which specifies clipping region of the page. Should have the following fields:
            x <number> x-coordinate of top-left corner of clip area
            y <number> y-coordinate of top-left corner of clip area
            width <number> width of clipping area
            height <number> height of clipping area
        omitBackground <boolean> Hides default white background and allows capturing screenshots with transparency. Defaults to false.
        """
        await element.screenshot(element, type=type, fullPage=fullPage, omitBackground=omitBackground, **kwargs)

    def get_screeshot(self, type='png', fullPage=False, omitBackground=False, **kwargs):
        """
        path     <string> The file path to save the image to. The screenshot type will be inferred from file extension. If path is a relative path, then it is resolved relative to current working directory. If no path is provided, the image won't be saved to the disk.
        type     <string> Specify screenshot type, can be either jpeg or png. Defaults to 'png'.
        quality  <number> The quality of the image, between 0-100. Not applicable to png images.
        fullPage <boolean> When true, takes a screenshot of the full scrollable page. Defaults to false.
        clip     <dict> An object which specifies clipping region of the page. Should have the following fields:
            x <number> x-coordinate of top-left corner of clip area
            y <number> y-coordinate of top-left corner of clip area
            width <number> width of clipping area
            height <number> height of clipping area
        omitBackground <boolean> Hides default white background and allows capturing screenshots with transparency. Defaults to false.
        """
        asyncio.get_event_loop().run_until_complete(self.__get_screenshot(self.element, type=type, fullPage=fullPage,
                                                                            omitBackground=omitBackground, **kwargs))

