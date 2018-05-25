# encoding: utf-8
from common.driver import Driver
from config import DEFAULT_CONFIG


class WebDriver(Driver):

    def __init__(self, headless=False, args=DEFAULT_CONFIG, timeout=30000, slow=0, ignoreHttpsErrors=False, execute_path=None,
                 signore_kill=True, data_dir=None):
        super().__init__(headless, args, timeout, slow, ignoreHttpsErrors, execute_path, signore_kill, data_dir)


if __name__ == "__main__":
    browser = WebDriver(headless=False)
    browser.current_page.request("https://www.baidu.com")
    print(browser.current_page.get_page_content())
    browser.current_page.wait_for(60*100)
    browser.current_page.close()
