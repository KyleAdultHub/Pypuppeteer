# encoding: utf-8
from common.driver import Driver
from config import DEFAULT_CONFIG


class WebDriverHeadless(Driver):

    def __init__(self, headless=True, args=DEFAULT_CONFIG, timeout=30000, slow=0, ignoreHttpsErrors=False, execute_path=None,
                 signore_kill=True, data_dir=None):
        super().__init__(headless, args, timeout, slow, ignoreHttpsErrors, execute_path, signore_kill, data_dir)