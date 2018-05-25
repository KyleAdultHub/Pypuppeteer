# encoding: utf-8
import asyncio
from common.response import Response
from common.element import Element
from common.frame import Frame


class Page(object):

    def __init__(self, page):
        self.page = page

    @staticmethod
    async def __get_page_content(page):
        """
        get the full html contents of this page, including the doctype.
        :param driver:
        :return:
        """
        return await page.content()

    def get_page_content(self):
        """
        get the full html contents of this page, including the doctype.
        :param driver:
        :return:
        """
        content = asyncio.get_event_loop().run_until_complete(self.__get_page_content(self.page))
        return content

    @staticmethod
    async def __get_cookies(page, url):
        """
        get the cookies for this driver , for this url
        :param page:
        :param url: string of url
        :return:
        """
        return await page.cookies(url)

    def get_cookies(self, urls):
        """
        get the cookies for this driver , for this url
        :param dirver:
        :param url: string of url
        :return:
        """
        cookies = asyncio.get_event_loop().run_until_complete(self.__get_cookies(self.page, urls))
        return cookies

    @staticmethod
    async def __request(page, url, timeout=None):
        """
        parse url
        :param page:
        :param url: the target url you want to parse, and will return a detail html content
        :return:
        """
        if timeout:
            response = await page.goto(url, timeout=timeout)
            return response
        response = await page.goto(url)
        return response

    def request(self, url, timeout=None):
        """
        parse url
        :param timeout:
        :param page:
        :param url: the target url you want to parse, and will return a detail html content
        :return:
        """
        return Response(asyncio.get_event_loop().run_until_complete(self.__request(self.page, url, timeout=timeout)))

    @staticmethod
    async def __click(page, selector, button='left', click_count=1, delay=0):
        """
        search for element to click. If there are multiple elements satisfying the selector, the first will be clicked.
        :param selector: string, a selector to search for element to click
        :param click_count: click times
        :param delay: the time between mousedown and mouseup
        :return:
        """
        await page.click(selector, button=button, clickCount=click_count, delay=delay)

    def click(self, selector, button='left', click_count=1, delay=0):
        """
        search for element to click. If there are multiple elements satisfying the selector, the first will be clicked.
        :param page:
        :param button:
        :param selector: string, a selector to search for element to click
        :param click_count: click times
        :param delay: the time between mousedown and mouseup
        :return:
        """
        asyncio.get_event_loop().run_until_complete(self.__click(self.page, selector, button=button, click_count=click_count, delay=delay))

    @staticmethod
    async def __focus(page, selector):
        """
        search for element to focus
        :param selector: string, a selector to search for element to click
        :return:
        """
        await page.focus(selector)

    def focus(self, selector):
        """
        search for element to focus
        :param selector: string, a selector to search for element to click
        :return:
        """
        asyncio.get_event_loop().run_until_complete(self.__focus(self.page, selector))

    @staticmethod
    async def __close(page):
        """
        search for element to focus
        :param selector: string, a selector to search for element to click
        :return:
        """
        await page.close()

    def close(self):
        """
        search for element to focus
        :param selector: string, a selector to search for element to click
        :return:
        """
        asyncio.get_event_loop().run_until_complete(self.__close(self.page))

    def get_current_url(self):
        """
        get the current url of this page
        :param page: page object
        :return:
        """
        return self.page.url()

    @staticmethod
    async def __reload(page, timeout=0):
        """
        reload current page url
        :param page: page object
        :param timeout: defaults to 30 seconds, pass 0 to disable timeout
        :return:
        """
        return await page.reload(page, timeout=timeout)

    def reload(self, timeout=0):
        """
        reload current page url
        :param page: page object
        :param timeout: defaults to 30 seconds, pass 0 to disable timeout
        :return:
        """
        return Response(asyncio.get_event_loop().run_until_complete(self.__reload(self.page, timeout=timeout)))

    @staticmethod
    async def __type(page, selector, text, delay=0):
        """
        send text to text frame
        :param page:
        :param selector:
        :param text:
        :param delay:
        :return:
        """
        await page.type(selector, text, delay=delay)

    def type(self, selector, text, delay=0):
        """
        send text to text frame
        :param page:
        :param selector:
        :param text:
        :param delay:
        :return:
        """
        asyncio.get_event_loop().run_until_complete(self.__type(self.page, selector=selector, text=text, delay=delay))

    @staticmethod
    async def __get_element_by_selector(page, selector):
        """
        find element by selector , if not only one selector finded , default return first element
        :param page: page object
        :param selector:  the string to query element in the page source
        :return:
        """
        return await page.quirySelector(selector)

    def get_element_by_selector(self, selector):
        """
        find element by selector , if not only one selector finded , default return first element
        :param page: page object
        :param selector:  the string to query element in the page source
        :return:
        """
        return Element(asyncio.get_event_loop().run_until_complete(self.__get_element_by_selector(self.page, selector=selector)))

    @staticmethod
    async def __get_elements_by_selector(page, selector):
        """
        find element by selector ,
        :param page: page object
        :param selector:  the string to query element in the page source
        :return: list contain all element for selector
        """
        return await page.quirySelectorAll(selector)

    def get_elements_by_selector(self, selector):
        """
        find element by selector ,
        :param page: page object
        :param selector:  the string to query element in the page source
        :return: list contain all element for selector
        """
        return [Element(i) for i in asyncio.get_event_loop().run_until_complete(self.__get_elements_by_selector(self.page, selector=selector))]

    @staticmethod
    async def __get_elements_by_xpath(page, xpath):
        """
        find element by xpath
        :param page: page object
        :param xpath:  the string to query element in the page source
        :return: list contain all element for selector
        """
        return await page.xpath(xpath)

    def get_elements_by_xpath(self, xpath):
        """
        find element by xpath
        :param page: page object
        :param xpath:  the string to query element in the page source
        :return: list contain all element for selector
        """
        return [Element(i) for i in asyncio.get_event_loop().run_until_complete(self.__get_elements_by_xpath(self.page, xpath=xpath))]

    @staticmethod
    async def __evaluate(page, pageFunction, *args, force_expr=False):
        """
        :param pageFunction: Function to be evaluated in browser context
        :param args:Arguments to pass to pageFunction
        :return:
        """
        if force_expr:
            return await page.evaluate(pageFunction, force_expr=force_expr)
        else:
            return await page.evaluate(pageFunction, *args)

    def evaluate(self, pageFunction, *args, force_expr=False):
        """
        :param force_expr:
        :param pageFunction: Function to be evaluated in browser context
        :param args:Arguments to pass to pageFunction
        :return:
        """
        return asyncio.get_event_loop().run_until_complete(self.__evaluate(self.page, pageFunction, *args, force_expr=force_expr))

    @staticmethod
    async def __setUserAgent(page, userAgent):
        await page.setUserAgent(userAgent=userAgent)

    def set_user_agent(self, userAgent):
        return asyncio.get_event_loop().run_until_complete(self.__setUserAgent(self.page, userAgent))

    @staticmethod
    async def __setViewport(page, width, height):
        await page.setViewport(width=width, height=height)

    def set_view_port(self, width, height):
        asyncio.get_event_loop().run_until_complete(self.__setViewport(self.page, width, height))

    @staticmethod
    async def __waitFor(page, timeout):
        """
        wait for some time
        """
        watch_dag = page.waitFor(timeout)
        return await watch_dag

    def wait_for(self, timeout=0):
        return Element(asyncio.get_event_loop().run_until_complete(self.__waitFor(self.page, timeout=timeout)))

    @staticmethod
    async def __waitForFunction(page, pageFunction, *args, timeout=0):
        """
        :param page:
        :param pageFunction: Function to be evaluated in browser context
        :param timeout: int maximum time to wait for in milliseconds. Defaults to 30000 (30 seconds). Pass 0 to disable timeout.
        :param args:  Arguments to pass to pageFunction
        :return:
        """
        watch_dag = page.waitForFunction(pageFunction, *args, timeout=timeout)
        return await watch_dag

    def wait_for_function(self, pageFunction, *args, timeout=0):
        """
        :param page:
        :param pageFunction: Function to be evaluated in browser context
        :param timeout: int maximum time to wait for in milliseconds. Defaults to 30000 (30 seconds). Pass 0 to disable timeout.
        :param args:  Arguments to pass to pageFunction
        :return:
        """
        return Element(asyncio.get_event_loop().run_until_complete(self.__waitForFunction(self.page, pageFunction, *args, timeout=timeout)))

    @staticmethod
    async def __waitForSelector(page, selector, timeout=0):
        """
        :param page:
        :param selector:
        :param timeout:
        :return:
        """
        watch_dag = page.waitForSelector(selector, timeout=timeout)
        return await watch_dag

    def wait_for_selector(self, selector, timeout=0):
        """
        :param selector:
        :param page:
        :param timeout:
        :return:
        """
        return Element(asyncio.get_event_loop().run_until_complete(self.__waitForSelector(self.page, selector, timeout=timeout)))

    @staticmethod
    async def __waitForXpath(page, xpath, timeout=0):
        """
        :param page:
        :param xpath:
        :param timeout:
        :return:
        """
        watch_dag = page.waitForXpath(xpath, timeout=timeout)
        return await watch_dag

    def wait_for_xpath(self, xpath, timeout=0):
        return Element(asyncio.get_event_loop().run_until_complete(self.__waitForXpath(self.page, xpath, timeout=timeout)))

    def get_frames(self):
        return [Frame(i) for i in self.page.frames]

    def get_main_frame(self):
        return Frame(self.page.mainFrame())

    @staticmethod
    async def __get_screenshot(page, type='png', fullPage=False, omitBackground=False, **kwargs):
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
        await page.screenshot(page, type=type, fullPage=fullPage, omitBackground=omitBackground, **kwargs)

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
        asyncio.get_event_loop().run_until_complete(self.__get_screenshot(self.page, type=type, fullPage=fullPage,
                                                                            omitBackground=omitBackground, **kwargs))

    @staticmethod
    async def __get_page_accurate_content(page, url):
        resource = await page._client.send('Page.getResourceTree')
        _id = resource.get('frameTree').get('frame').get('id')
        content = await page._client.send('Page.getResourceContent', {"frameId": _id, "url": url})
        return content

    def get_page_accurate_content(self, url):
        return self.__get_page_accurate_content(self.page, url)

    def add_listener(self, event, call_back):
        """
        :param page:page object
        :param call_back:  the function of once event is listened
        :return:
        """
        self.page.on(event, call_back)