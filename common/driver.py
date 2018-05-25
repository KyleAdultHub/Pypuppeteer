# encoding: utf-8
import asyncio
from pyppeteer import launch
import platform
from common.page import Page


class Driver(object):

    def __init__(self, headless=False,
                      args=None, timeout=30000,
                      slow=0, ignoreHttpsErrors=False,
                      execute_path=None, signore_kill=True,
                      data_dir=None):
        self.driver = None
        self.create_driver(headless=headless,
                      args=args, timeout=timeout,
                      slow=slow, ignoreHttpsErrors=ignoreHttpsErrors,
                      execute_path=execute_path, signore_kill=signore_kill,
                      data_dir=data_dir)
        self.current_page = self.get_pages()[0]

    @staticmethod
    async def __create_driver(headless=False,
                              args=None, timeout=30000,
                              slow=0, ignoreHttpsErrors=False,
                              execute_path=None, signore_kill=True,
                              data_dir=None):
        if args is None:
            args = []
        if not data_dir:
            if platform.system() == "Windows":
                data_dir = r"C:/Users{USER}/AppData/Local/Google/Chrome/User Data"
            else:
                data_dir = r"~/.config"
        if execute_path:
            driver = await launch(headless=headless, args=args,
                                  timeout=timeout, slowMo=0,
                                  ignoreHttpsErrors=ignoreHttpsErrors,
                                  executablePath=execute_path,
                                  handleSIGINT=signore_kill,
                                  userDataDir=data_dir
                                  )
        else:
            driver = await launch(headless=headless, args=args,
                                  timeout=timeout, slowMo=slow,
                                  ignoreHttpsErrors=ignoreHttpsErrors,
                                  handleSIGINT=signore_kill,
                                  userDataDir=data_dir
                                  )
        return driver

    def create_driver(self, headless=False,
                      args=None, timeout=30000,
                      slow=0, ignoreHttpsErrors=False,
                      execute_path=None, signore_kill=True,
                      data_dir=None
                      ):
        """
        create driver of chrome
        :param headless:
        :param args:
        :param timeout:
        :param slow:
        :param ignoreHttpsErrors:
        :param execute_path:
        :param signore_kill:
        :param data_dir:
        :return:
        """
        self.driver = asyncio.get_event_loop().run_until_complete(self.__create_driver(headless=headless,
                                                                             args=args, timeout=timeout,
                                                                             slow=slow, ignoreHttpsErrors=ignoreHttpsErrors,
                                                                             execute_path=execute_path, signore_kill=signore_kill,
                                                                             data_dir=data_dir
                                                                             ))

    @staticmethod
    async def __create_page(driver):
        page = await driver.newPage()
        return page

    def create_page(self):
        """
        create a page of driver
        :param driver:
        :return:
        """
        page = asyncio.get_event_loop().run_until_complete(self.__create_page(self.driver))
        self.current_page = Page(page)
        return self.current_page

    @staticmethod
    async def __get_pages(driver):
        pages = await driver.pages()
        return pages

    def get_pages(self):
        """
        get all pages of current driver
        :param driver:
        :return:
        """
        pages = asyncio.get_event_loop().run_until_complete(self.__get_pages(self.driver))
        return [Page(i) for i in pages]

    @staticmethod
    async def __set_userAgent(driver, userAgent):
        """
        set driver user_agent , can resolves to the browser's original user agent.
        :param driver:
        :return:
        """
        await driver.userAgent(userAgent)

    def ser_userAgent(self, userAgent):
        """
        set driver user_agent , can resolves to the browser's original user agent.
        :param driver:
        :return:
        """
        asyncio.get_event_loop().run_until_complete(self.__set_userAgent(self.driver, userAgent))

    @staticmethod
    async def __close_driver(driver):
        """
        close the driver of chrome
        :param driver:
        :return:
        """
        await driver.close()

    def close_driver(self):
        """
        set driver user_agent , can resolves to the browser's original user agent.
        :param driver:
        :return:
        """
        asyncio.get_event_loop().run_until_complete(self.__close_driver(self.driver))

    def change_page(self, page_index):
        self.current_page = self.get_pages()[page_index]

    def __del__(self):
        self.close_driver()


if __name__ == "__main__":
    # driver = create_driver()
    # time.sleep(5)
    # # close_driver(driver)
    pass
